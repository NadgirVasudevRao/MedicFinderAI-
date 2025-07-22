"""
Indian hospital data with comprehensive information including specialties,
ratings, NABH accreditation, and insurance acceptance.
"""

HOSPITALS_DATA = [
    # Delhi Hospitals
    {
        "name": "All India Institute of Medical Sciences (AIIMS)",
        "address": "Ansari Nagar, New Delhi - 110029",
        "city": "New Delhi",
        "state": "Delhi",
        "latitude": 28.5672,
        "longitude": 77.2100,
        "type": "Government",
        "rating": 4.8,
        "specialties": ["Cardiology", "Oncology", "Neurology", "Orthopedics", "General Surgery"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ECHS", "Ayushman Bharat", "Private Insurance"],
        "phone": "+91-11-26588500",
        "website": "https://aiims.edu"
    },
    {
        "name": "Sir Ganga Ram Hospital",
        "address": "Rajinder Nagar, New Delhi - 110060",
        "city": "New Delhi",
        "state": "Delhi",
        "latitude": 28.6369,
        "longitude": 77.1926,
        "type": "Private",
        "rating": 4.6,
        "specialties": ["Cardiology", "Gastroenterology", "Nephrology", "Urology", "Pulmonology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "Bajaj Allianz"],
        "phone": "+91-11-25750000"
    },
    {
        "name": "Fortis Hospital Shalimar Bagh",
        "address": "A Block, Shalimar Bagh, New Delhi - 110088",
        "city": "New Delhi",
        "state": "Delhi",
        "latitude": 28.7196,
        "longitude": 77.1564,
        "type": "Private",
        "rating": 4.4,
        "specialties": ["Cardiology", "Oncology", "Orthopedics", "Neurology", "Pediatrics"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Max Bupa", "Star Health", "New India Assurance", "Oriental Insurance"]
    },
    
    # Mumbai Hospitals
    {
        "name": "Tata Memorial Hospital",
        "address": "Dr Ernest Borges Marg, Parel, Mumbai - 400012",
        "city": "Mumbai",
        "state": "Maharashtra",
        "latitude": 19.0176,
        "longitude": 72.8562,
        "type": "Government",
        "rating": 4.7,
        "specialties": ["Oncology", "Radiation Therapy", "Surgical Oncology", "Medical Oncology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat", "Private Insurance"]
    },
    {
        "name": "Kokilaben Dhirubhai Ambani Hospital",
        "address": "Rao Saheb Achutrao Patwardhan Marg, Four Bunglows, Andheri West, Mumbai - 400053",
        "city": "Mumbai",
        "state": "Maharashtra",
        "latitude": 19.1136,
        "longitude": 72.8305,
        "type": "Private",
        "rating": 4.5,
        "specialties": ["Cardiology", "Neurology", "Oncology", "Transplant Surgery", "Robotic Surgery"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["HDFC ERGO", "ICICI Lombard", "Bajaj Allianz", "Star Health"]
    },
    {
        "name": "Lilavati Hospital",
        "address": "A-791, Bandra Reclamation, Bandra West, Mumbai - 400050",
        "city": "Mumbai",
        "state": "Maharashtra",
        "latitude": 19.0596,
        "longitude": 72.8295,
        "type": "Private",
        "rating": 4.3,
        "specialties": ["Cardiology", "Orthopedics", "Neurology", "Gastroenterology", "Urology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "Max Bupa", "Religare Health", "Care Health"]
    },
    
    # Bangalore Hospitals
    {
        "name": "Narayana Health City",
        "address": "258/A, Bommasandra Industrial Area, Anekal Taluk, Bengaluru - 560099",
        "city": "Bangalore",
        "state": "Karnataka",
        "latitude": 12.8057,
        "longitude": 77.7532,
        "type": "Private",
        "rating": 4.6,
        "specialties": ["Cardiology", "Cardiac Surgery", "Oncology", "Neurology", "Transplant"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "New India Assurance"]
    },
    {
        "name": "Manipal Hospital Bangalore",
        "address": "98, Rustum Bagh, Airport Road, Bengaluru - 560017",
        "city": "Bangalore",
        "state": "Karnataka",
        "latitude": 13.0067,
        "longitude": 77.5540,
        "type": "Private",
        "rating": 4.4,
        "specialties": ["Orthopedics", "Neurology", "Cardiology", "Gastroenterology", "Urology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Bajaj Allianz", "Star Health", "Max Bupa", "Care Health"]
    },
    {
        "name": "Kidwai Memorial Institute of Oncology",
        "address": "Dr M H Marigowda Rd, Bengaluru - 560029",
        "city": "Bangalore",
        "state": "Karnataka",
        "latitude": 12.9539,
        "longitude": 77.5958,
        "type": "Government",
        "rating": 4.5,
        "specialties": ["Oncology", "Radiation Therapy", "Surgical Oncology", "Chemotherapy"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat"]
    },
    
    # Chennai Hospitals
    {
        "name": "Apollo Hospital Chennai",
        "address": "21, Greams Lane, Off Greams Road, Chennai - 600006",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "latitude": 13.0569,
        "longitude": 80.2495,
        "type": "Private",
        "rating": 4.7,
        "specialties": ["Cardiology", "Transplant Surgery", "Oncology", "Neurology", "Orthopedics"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "Bajaj Allianz"]
    },
    {
        "name": "Fortis Malar Hospital",
        "address": "52, 1st Main Road, Gandhinagar, Adyar, Chennai - 600020",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "latitude": 13.0067,
        "longitude": 80.2568,
        "type": "Private",
        "rating": 4.5,
        "specialties": ["Cardiology", "Orthopedics", "Neurology", "Gastroenterology", "Nephrology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Max Bupa", "Star Health", "Care Health", "Religare Health"]
    },
    {
        "name": "Government General Hospital Chennai",
        "address": "EVR Periyar Salai, Park Town, Chennai - 600003",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "latitude": 13.0878,
        "longitude": 80.2785,
        "type": "Government",
        "rating": 4.2,
        "specialties": ["General Medicine", "Surgery", "Pediatrics", "Obstetrics", "Emergency Medicine"],
        "nabh_accredited": False,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat"]
    },
    
    # Hyderabad Hospitals
    {
        "name": "Asian Institute of Gastroenterology",
        "address": "6-3-661, Somajiguda, Hyderabad - 500082",
        "city": "Hyderabad",
        "state": "Telangana",
        "latitude": 17.4126,
        "longitude": 78.4654,
        "type": "Private",
        "rating": 4.6,
        "specialties": ["Gastroenterology", "Hepatology", "Liver Transplant", "Endoscopy"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "New India Assurance"]
    },
    {
        "name": "Apollo Hospital Hyderabad",
        "address": "Jubilee Hills, Hyderabad - 500033",
        "city": "Hyderabad",
        "state": "Telangana",
        "latitude": 17.4399,
        "longitude": 78.4037,
        "type": "Private",
        "rating": 4.5,
        "specialties": ["Cardiology", "Oncology", "Neurology", "Orthopedics", "Transplant"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Bajaj Allianz", "Star Health", "Max Bupa", "Care Health"]
    },
    {
        "name": "Nizam's Institute of Medical Sciences",
        "address": "Punjagutta, Hyderabad - 500082",
        "city": "Hyderabad",
        "state": "Telangana",
        "latitude": 17.4239,
        "longitude": 78.4738,
        "type": "Government",
        "rating": 4.4,
        "specialties": ["Cardiology", "Neurology", "Nephrology", "Gastroenterology", "Emergency Medicine"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat", "Private Insurance"]
    },
    
    # Kolkata Hospitals
    {
        "name": "AMRI Hospital Kolkata",
        "address": "P-4 & 5, CIT Scheme LXXII, Action Area IIC, Newtown, Kolkata - 700156",
        "city": "Kolkata",
        "state": "West Bengal",
        "latitude": 22.5958,
        "longitude": 88.4154,
        "type": "Private",
        "rating": 4.4,
        "specialties": ["Cardiology", "Oncology", "Orthopedics", "Neurology", "Gastroenterology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "Bajaj Allianz"]
    },
    {
        "name": "Medical College and Hospital Kolkata",
        "address": "88, College Street, Kolkata - 700073",
        "city": "Kolkata",
        "state": "West Bengal",
        "latitude": 22.5958,
        "longitude": 88.3639,
        "type": "Government",
        "rating": 4.1,
        "specialties": ["General Medicine", "Surgery", "Pediatrics", "Obstetrics", "Emergency Medicine"],
        "nabh_accredited": False,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat"]
    },
    {
        "name": "Fortis Hospital Kolkata",
        "address": "730, Anandapur, E M Bypass Road, Kolkata - 700107",
        "city": "Kolkata",
        "state": "West Bengal",
        "latitude": 22.5091,
        "longitude": 88.3967,
        "type": "Private",
        "rating": 4.3,
        "specialties": ["Cardiology", "Neurology", "Orthopedics", "Oncology", "Nephrology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Max Bupa", "Star Health", "Care Health", "Religare Health"]
    },
    
    # Pune Hospitals
    {
        "name": "Ruby Hall Clinic",
        "address": "40, Sassoon Road, Pune - 411001",
        "city": "Pune",
        "state": "Maharashtra",
        "latitude": 18.5314,
        "longitude": 73.8695,
        "type": "Private",
        "rating": 4.5,
        "specialties": ["Cardiology", "Neurology", "Orthopedics", "Oncology", "Gastroenterology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "Bajaj Allianz"]
    },
    {
        "name": "Sassoon General Hospital",
        "address": "Near Pune Railway Station, Pune - 411001",
        "city": "Pune",
        "state": "Maharashtra",
        "latitude": 18.5204,
        "longitude": 73.8567,
        "type": "Government",
        "rating": 4.0,
        "specialties": ["General Medicine", "Surgery", "Emergency Medicine", "Trauma Care", "Pediatrics"],
        "nabh_accredited": False,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat"]
    },
    {
        "name": "Manipal Hospital Pune",
        "address": "#1, Bhat Estate, Off Viman Nagar Road, Pune - 411014",
        "city": "Pune",
        "state": "Maharashtra",
        "latitude": 18.5679,
        "longitude": 73.9143,
        "type": "Private",
        "rating": 4.4,
        "specialties": ["Orthopedics", "Neurology", "Cardiology", "Urology", "Gastroenterology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Bajaj Allianz", "Star Health", "Max Bupa", "Care Health"]
    },
    
    # Ahmedabad Hospitals
    {
        "name": "Sterling Hospital Ahmedabad",
        "address": "Off Gurukul Road, Memnagar, Ahmedabad - 380052",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "latitude": 23.0593,
        "longitude": 72.5404,
        "type": "Private",
        "rating": 4.4,
        "specialties": ["Cardiology", "Oncology", "Neurology", "Orthopedics", "Gastroenterology"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Star Health", "HDFC ERGO", "ICICI Lombard", "New India Assurance"]
    },
    {
        "name": "Civil Hospital Ahmedabad",
        "address": "Asarwa, Ahmedabad - 380016",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "latitude": 23.0395,
        "longitude": 72.5658,
        "type": "Government",
        "rating": 3.8,
        "specialties": ["General Medicine", "Surgery", "Emergency Medicine", "Pediatrics", "Obstetrics"],
        "nabh_accredited": False,
        "emergency_services": True,
        "insurance_accepted": ["CGHS", "ESI", "Ayushman Bharat"]
    },
    {
        "name": "Apollo Hospital Ahmedabad",
        "address": "Plot No 1A, Bhat GIDC Estate, Gandhinagar - 382428",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "latitude": 23.2156,
        "longitude": 72.6369,
        "type": "Private",
        "rating": 4.3,
        "specialties": ["Cardiology", "Transplant Surgery", "Oncology", "Neurology", "Orthopedics"],
        "nabh_accredited": True,
        "emergency_services": True,
        "insurance_accepted": ["Bajaj Allianz", "Star Health", "Max Bupa", "Care Health"]
    }
]

def get_hospitals_by_location(city, state=None):
    """Get hospitals filtered by city and optionally by state"""
    filtered_hospitals = []
    
    for hospital in HOSPITALS_DATA:
        if city.lower() in hospital['city'].lower():
            if state is None or state.lower() in hospital['state'].lower():
                filtered_hospitals.append(hospital)
    
    return filtered_hospitals

def get_hospitals_by_specialty(specialty):
    """Get hospitals that have the specified specialty"""
    specialty_hospitals = []
    
    for hospital in HOSPITALS_DATA:
        for hosp_specialty in hospital['specialties']:
            if specialty.lower() in hosp_specialty.lower():
                specialty_hospitals.append(hospital)
                break
    
    return specialty_hospitals
