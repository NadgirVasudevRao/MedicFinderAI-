"""
Distance calculation utilities for Indian hospital finder.
Handles coordinate-based distance calculations and travel time estimates.
"""

from geopy.distance import geodesic
import math

def calculate_distance(coord1, coord2):
    """
    Calculate distance between two coordinates using geodesic calculation.
    
    Args:
        coord1: Tuple of (latitude, longitude) for first location
        coord2: Tuple of (latitude, longitude) for second location
    
    Returns:
        Distance in kilometers (float)
    """
    try:
        distance = geodesic(coord1, coord2).kilometers
        return round(distance, 2)
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return 0.0

def calculate_travel_time(distance_km, mode="car"):
    """
    Estimate travel time based on distance and mode of transport.
    
    Args:
        distance_km: Distance in kilometers
        mode: Mode of transport ("car", "bike", "walk", "public_transport")
    
    Returns:
        Travel time in minutes
    """
    # Average speeds in km/h for different modes in Indian conditions
    speeds = {
        "car": 25,  # Accounting for Indian traffic conditions
        "bike": 20,
        "walk": 4,
        "public_transport": 15,
        "auto_rickshaw": 18
    }
    
    speed = speeds.get(mode, 25)
    time_hours = distance_km / speed
    time_minutes = time_hours * 60
    
    return round(time_minutes, 0)

def get_distance_category(distance_km):
    """
    Categorize distance into ranges.
    
    Args:
        distance_km: Distance in kilometers
    
    Returns:
        String category ("Very Near", "Near", "Moderate", "Far", "Very Far")
    """
    if distance_km <= 2:
        return "Very Near"
    elif distance_km <= 5:
        return "Near"
    elif distance_km <= 15:
        return "Moderate"
    elif distance_km <= 30:
        return "Far"
    else:
        return "Very Far"

def find_nearest_hospitals(user_location, hospitals, max_distance=50):
    """
    Find hospitals within a specified distance from user location.
    
    Args:
        user_location: Tuple of (latitude, longitude)
        hospitals: List of hospital dictionaries with latitude and longitude
        max_distance: Maximum distance in kilometers
    
    Returns:
        List of hospitals with distance information, sorted by distance
    """
    nearby_hospitals = []
    
    for hospital in hospitals:
        try:
            hospital_location = (hospital['latitude'], hospital['longitude'])
            distance = calculate_distance(user_location, hospital_location)
            
            if distance <= max_distance:
                hospital_with_distance = hospital.copy()
                hospital_with_distance['distance'] = distance
                hospital_with_distance['distance_category'] = get_distance_category(distance)
                hospital_with_distance['travel_time_car'] = calculate_travel_time(distance, "car")
                hospital_with_distance['travel_time_public'] = calculate_travel_time(distance, "public_transport")
                nearby_hospitals.append(hospital_with_distance)
        
        except Exception as e:
            print(f"Error processing hospital {hospital.get('name', 'Unknown')}: {e}")
            continue
    
    # Sort by distance
    nearby_hospitals.sort(key=lambda x: x['distance'])
    return nearby_hospitals

def calculate_area_coverage(center_location, radius_km):
    """
    Calculate approximate area coverage for hospital search.
    
    Args:
        center_location: Tuple of (latitude, longitude)
        radius_km: Search radius in kilometers
    
    Returns:
        Dictionary with coverage area information
    """
    # Rough approximation: 1 degree latitude ≈ 111 km
    lat_degree_km = 111
    lng_degree_km = lat_degree_km * math.cos(math.radians(center_location[0]))
    
    lat_range = radius_km / lat_degree_km
    lng_range = radius_km / lng_degree_km
    
    return {
        "center": center_location,
        "radius_km": radius_km,
        "lat_min": center_location[0] - lat_range,
        "lat_max": center_location[0] + lat_range,
        "lng_min": center_location[1] - lng_range,
        "lng_max": center_location[1] + lng_range,
        "area_sq_km": math.pi * (radius_km ** 2)
    }

def is_within_bounds(location, bounds):
    """
    Check if a location is within specified geographical bounds.
    
    Args:
        location: Tuple of (latitude, longitude)
        bounds: Dictionary with lat_min, lat_max, lng_min, lng_max
    
    Returns:
        Boolean indicating if location is within bounds
    """
    lat, lng = location
    return (bounds['lat_min'] <= lat <= bounds['lat_max'] and 
            bounds['lng_min'] <= lng <= bounds['lng_max'])

def get_distance_text(distance_km):
    """
    Convert distance to human-readable text.
    
    Args:
        distance_km: Distance in kilometers
    
    Returns:
        Formatted distance string
    """
    if distance_km < 1:
        meters = distance_km * 1000
        return f"{meters:.0f} meters"
    elif distance_km < 10:
        return f"{distance_km:.1f} km"
    else:
        return f"{distance_km:.0f} km"
