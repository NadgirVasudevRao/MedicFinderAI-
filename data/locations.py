"""
Indian states, cities, and geographical coordinates for location-based hospital search.
"""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Major Indian locations with coordinates
INDIAN_LOCATIONS = {
    "Delhi": ["New Delhi", "Central Delhi", "North Delhi", "South Delhi", "East Delhi", "West Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Thane", "Navi Mumbai", "Kolhapur", "Sangli"],
    "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum", "Davangere", "Bellary", "Bijapur", "Shimoga", "Tumkur"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Erode", "Vellore", "Thoothukudi", "Dindigul"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam", "Ramagundam", "Mahbubnagar", "Nalgonda", "Adilabad", "Miryalaguda"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Malda", "Bardhaman", "Baharampur", "Habra", "Kharagpur"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Nadiad", "Morbi", "Surendranagar", "Bharuch"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer", "Udaipur", "Bhilwara", "Alwar", "Bharatpur", "Pali"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Ghaziabad", "Agra", "Varanasi", "Meerut", "Allahabad", "Bareilly", "Aligarh", "Moradabad"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain", "Sagar", "Dewas", "Satna", "Ratlam", "Rewa"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Purnia", "Darbhanga", "Bihar Sharif", "Arrah", "Begusarai", "Katihar"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Brahmapur", "Sambalpur", "Puri", "Balasore", "Bhadrak", "Baripada", "Jharsuguda"],
    "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Mohali", "Firozpur", "Batala", "Pathankot"],
    "Haryana": ["Faridabad", "Gurgaon", "Hisar", "Rohtak", "Panipat", "Karnal", "Sonipat", "Yamunanagar", "Panchkula", "Bhiwani"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Nagaon", "Tinsukia", "Tezpur", "Bongaigaon", "Dhubri", "North Lakhimpur"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kollam", "Palakkad", "Alappuzha", "Malappuram", "Kannur", "Kasaragod"],
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool", "Rajahmundry", "Tirupati", "Kadapa", "Kakinada", "Anantapur"]
}

# Predefined coordinates for major cities to avoid API calls
CITY_COORDINATES = {
    # Delhi
    "new delhi": (28.6139, 77.2090),
    "delhi": (28.6139, 77.2090),
    "gurgaon": (28.4595, 77.0266),
    "noida": (28.5355, 77.3910),
    
    # Maharashtra
    "mumbai": (19.0760, 72.8777),
    "pune": (18.5204, 73.8567),
    "nagpur": (21.1458, 79.0882),
    "nashik": (19.9975, 73.7898),
    "thane": (19.2183, 72.9781),
    
    # Karnataka
    "bangalore": (12.9716, 77.5946),
    "bengaluru": (12.9716, 77.5946),
    "mysore": (12.2958, 76.6394),
    "hubli": (15.3647, 75.1240),
    "mangalore": (12.9141, 74.8560),
    
    # Tamil Nadu
    "chennai": (13.0827, 80.2707),
    "coimbatore": (11.0168, 76.9558),
    "madurai": (9.9252, 78.1198),
    "salem": (11.6643, 78.1460),
    
    # Telangana
    "hyderabad": (17.3850, 78.4867),
    "warangal": (17.9689, 79.5941),
    "nizamabad": (18.6725, 78.0941),
    
    # West Bengal
    "kolkata": (22.5726, 88.3639),
    "howrah": (22.5958, 88.2636),
    "durgapur": (23.5204, 87.3119),
    "siliguri": (26.7271, 88.3953),
    
    # Gujarat
    "ahmedabad": (23.0225, 72.5714),
    "surat": (21.1702, 72.8311),
    "vadodara": (22.3072, 73.1812),
    "rajkot": (22.3039, 70.8022),
    
    # Rajasthan
    "jaipur": (26.9124, 75.7873),
    "jodhpur": (26.2389, 73.0243),
    "udaipur": (24.5854, 73.7125),
    "kota": (25.2138, 75.8648),
    
    # Uttar Pradesh
    "lucknow": (26.8467, 80.9462),
    "kanpur": (26.4499, 80.3319),
    "agra": (27.1767, 78.0081),
    "varanasi": (25.3176, 82.9739),
    
    # Other major cities
    "bhopal": (23.2599, 77.4126),
    "indore": (22.7196, 75.8577),
    "patna": (25.5941, 85.1376),
    "bhubaneswar": (20.2961, 85.8245),
    "chandigarh": (30.7333, 76.7794),
    "guwahati": (26.1445, 91.7362),
    "thiruvananthapuram": (8.5241, 76.9366),
    "kochi": (9.9312, 76.2673),
    "visakhapatnam": (17.6868, 83.2185)
}

def get_coordinates(location_string):
    """
    Get coordinates for a location string.
    First tries the predefined coordinates, then falls back to geocoding.
    """
    # Clean and normalize the location string
    location_clean = location_string.lower().strip()
    
    # Remove common suffixes and prefixes
    location_clean = location_clean.replace(" district", "").replace(" city", "")
    
    # Try to find in predefined coordinates
    for city, coords in CITY_COORDINATES.items():
        if city in location_clean or location_clean in city:
            return coords
    
    # Fall back to geocoding for more specific locations
    try:
        geolocator = Nominatim(user_agent="indian_hospital_finder")
        # Add "India" to improve geocoding accuracy
        search_location = f"{location_string}, India"
        location = geolocator.geocode(search_location, timeout=10)
        
        if location:
            return (location.latitude, location.longitude)
        else:
            # Try without "India" suffix
            location = geolocator.geocode(location_string, timeout=10)
            if location:
                return (location.latitude, location.longitude)
    
    except (GeocoderTimedOut, Exception) as e:
        print(f"Geocoding failed for {location_string}: {e}")
    
    # If all else fails, return None
    return None

def get_nearby_cities(state, target_city):
    """Get list of cities in the same state for nearby search"""
    if state in INDIAN_LOCATIONS:
        cities = INDIAN_LOCATIONS[state].copy()
        if target_city in cities:
            cities.remove(target_city)
        return cities
    return []

def is_indian_location(location_string):
    """Check if a location string appears to be in India"""
    location_lower = location_string.lower()
    
    # Check if it contains any Indian state or major city names
    for state, cities in INDIAN_LOCATIONS.items():
        if state.lower() in location_lower:
            return True
        for city in cities:
            if city.lower() in location_lower:
                return True
    
    # Check predefined coordinates
    for city in CITY_COORDINATES.keys():
        if city in location_lower:
            return True
    
    return False
