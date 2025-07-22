"""
AI-powered hospital matching system for Indian healthcare.
Matches hospitals to medical conditions based on specialties, ratings, and other factors.
"""

import random
from data.conditions import get_condition_specialties, is_emergency_condition
from data.hospitals import HOSPITALS_DATA, get_hospitals_by_specialty
from data.locations import get_coordinates
from utils.distance import calculate_distance, find_nearest_hospitals

def calculate_specialty_match_score(condition, hospital_specialties):
    """
    Calculate how well hospital specialties match the medical condition.
    
    Args:
        condition: Medical condition string
        hospital_specialties: List of hospital specialties
    
    Returns:
        Match score from 0 to 100
    """
    required_specialties = get_condition_specialties(condition)
    
    if not required_specialties:
        return 50  # Default score if no specific specialties found
    
    match_count = 0
    total_specialties = len(required_specialties)
    
    for required_spec in required_specialties:
        for hospital_spec in hospital_specialties:
            # Exact match
            if required_spec.lower() == hospital_spec.lower():
                match_count += 1
                break
            # Partial match
            elif (required_spec.lower() in hospital_spec.lower() or 
                  hospital_spec.lower() in required_spec.lower()):
                match_count += 0.7
                break
            # Related specialty match
            elif are_related_specialties(required_spec, hospital_spec):
                match_count += 0.5
                break
    
    # Calculate percentage match
    match_percentage = (match_count / total_specialties) * 100
    return min(100, max(0, match_percentage))

def are_related_specialties(spec1, spec2):
    """
    Check if two medical specialties are related.
    
    Args:
        spec1: First specialty
        spec2: Second specialty
    
    Returns:
        Boolean indicating if specialties are related
    """
    # Define related specialty groups
    related_groups = [
        ["Cardiology", "Cardiac Surgery", "Cardiovascular Surgery"],
        ["Neurology", "Neurosurgery", "Neurological Surgery"],
        ["Orthopedics", "Orthopedic Surgery", "Sports Medicine"],
        ["Gastroenterology", "Hepatology", "GI Surgery"],
        ["Oncology", "Surgical Oncology", "Medical Oncology", "Radiation Therapy"],
        ["Urology", "Nephrology", "Kidney Transplant"],
        ["Obstetrics", "Gynecology", "Reproductive Medicine"],
        ["Pediatrics", "Neonatology", "Pediatric Surgery"],
        ["Internal Medicine", "General Medicine", "Family Medicine"],
        ["Emergency Medicine", "Trauma Surgery", "Critical Care"],
        ["Psychiatry", "Psychology", "Mental Health"],
        ["Pulmonology", "Respiratory Medicine", "Thoracic Surgery"]
    ]
    
    spec1_lower = spec1.lower()
    spec2_lower = spec2.lower()
    
    for group in related_groups:
        group_lower = [s.lower() for s in group]
        if spec1_lower in group_lower and spec2_lower in group_lower:
            return True
    
    return False

def calculate_accessibility_score(hospital, user_location, hospital_type_preference):
    """
    Calculate hospital accessibility score based on various factors.
    
    Args:
        hospital: Hospital dictionary
        user_location: User's coordinates tuple
        hospital_type_preference: List of preferred hospital types
    
    Returns:
        Accessibility score from 0 to 100
    """
    score = 50  # Base score
    
    # Hospital type preference
    if hospital['type'] in hospital_type_preference:
        score += 20
    
    # Emergency services availability
    if hospital.get('emergency_services', False):
        score += 15
    
    # NABH accreditation
    if hospital.get('nabh_accredited', False):
        score += 10
    
    # Insurance acceptance (important in Indian context)
    if hospital.get('insurance_accepted'):
        score += 5
    
    return min(100, score)

def calculate_quality_score(hospital):
    """
    Calculate hospital quality score based on ratings and accreditations.
    
    Args:
        hospital: Hospital dictionary
    
    Returns:
        Quality score from 0 to 100
    """
    # Base score from rating (out of 5, converted to 100)
    rating_score = (hospital['rating'] / 5.0) * 60
    
    # NABH accreditation bonus
    nabh_bonus = 25 if hospital.get('nabh_accredited', False) else 0
    
    # Government hospital reliability bonus
    gov_bonus = 10 if hospital['type'] == 'Government' else 0
    
    # Emergency services bonus
    emergency_bonus = 5 if hospital.get('emergency_services', False) else 0
    
    total_score = rating_score + nabh_bonus + gov_bonus + emergency_bonus
    return min(100, total_score)

def calculate_ai_score(condition, hospital, user_location, preferences):
    """
    Calculate comprehensive AI matching score for hospital-condition pair.
    
    Args:
        condition: Medical condition
        hospital: Hospital dictionary
        user_location: User coordinates
        preferences: User preferences dictionary
    
    Returns:
        Overall AI score from 0 to 100
    """
    # Weight factors for different components
    weights = {
        'specialty_match': 0.4,
        'quality': 0.3,
        'accessibility': 0.2,
        'distance': 0.1
    }
    
    # Calculate component scores
    specialty_score = calculate_specialty_match_score(condition, hospital['specialties'])
    quality_score = calculate_quality_score(hospital)
    accessibility_score = calculate_accessibility_score(
        hospital, user_location, preferences.get('hospital_type', ['Government', 'Private'])
    )
    
    # Distance score (closer is better, max distance affects score)
    if user_location and 'latitude' in hospital and 'longitude' in hospital:
        distance = calculate_distance(
            user_location, 
            (hospital['latitude'], hospital['longitude'])
        )
        max_distance = preferences.get('max_distance', 50)
        distance_score = max(0, 100 - (distance / max_distance) * 100)
    else:
        distance_score = 50  # Default if distance can't be calculated
    
    # Emergency condition bonus
    emergency_bonus = 0
    if is_emergency_condition(condition) and hospital.get('emergency_services', False):
        emergency_bonus = 10
    
    # Calculate weighted score
    weighted_score = (
        specialty_score * weights['specialty_match'] +
        quality_score * weights['quality'] +
        accessibility_score * weights['accessibility'] +
        distance_score * weights['distance'] +
        emergency_bonus
    )
    
    return min(100, max(0, weighted_score))

def match_hospitals_to_condition(condition, user_location_str, hospital_types, min_rating, max_distance):
    """
    Main function to match hospitals to a medical condition using AI scoring.
    
    Args:
        condition: Medical condition string
        user_location_str: User location as string
        hospital_types: List of preferred hospital types
        min_rating: Minimum hospital rating
        max_distance: Maximum distance in kilometers
    
    Returns:
        List of matched hospitals with AI scores, sorted by score
    """
    user_coordinates = get_coordinates(user_location_str)
    
    if not user_coordinates:
        # If we can't get user coordinates, return all hospitals meeting basic criteria
        filtered_hospitals = []
        for hospital in HOSPITALS_DATA:
            if (hospital['type'] in hospital_types and 
                hospital['rating'] >= min_rating):
                filtered_hospitals.append(hospital)
        return filtered_hospitals[:20]
    
    # Find hospitals within distance
    nearby_hospitals = find_nearest_hospitals(
        user_coordinates, 
        HOSPITALS_DATA, 
        max_distance
    )
    
    # Apply rating and type filters
    filtered_hospitals = []
    for hospital in nearby_hospitals:
        if (hospital['type'] in hospital_types and 
            hospital['rating'] >= min_rating):
            filtered_hospitals.append(hospital)
    
    # Calculate AI scores
    preferences = {
        'hospital_type': hospital_types,
        'max_distance': max_distance,
        'min_rating': min_rating
    }
    
    scored_hospitals = []
    for hospital in filtered_hospitals:
        # Calculate individual component scores
        specialty_score = calculate_specialty_match_score(condition, hospital['specialties'])
        quality_score = calculate_quality_score(hospital)
        accessibility_score = calculate_accessibility_score(
            hospital, user_coordinates, preferences.get('hospital_type', ['Government', 'Private'])
        )
        
        # Calculate distance score
        if user_coordinates and 'latitude' in hospital and 'longitude' in hospital:
            distance = calculate_distance(
                user_coordinates, 
                (hospital['latitude'], hospital['longitude'])
            )
            max_distance = preferences.get('max_distance', 50)
            distance_score = max(0, 100 - (distance / max_distance) * 100)
        else:
            distance_score = 50
        
        # Calculate overall AI score
        ai_score = calculate_ai_score(
            condition, 
            hospital, 
            user_coordinates, 
            preferences
        )
        
        hospital_with_score = hospital.copy()
        hospital_with_score['ai_score'] = ai_score
        hospital_with_score['specialty_score'] = specialty_score
        hospital_with_score['quality_score'] = quality_score
        hospital_with_score['accessibility_score'] = accessibility_score
        hospital_with_score['distance_score'] = distance_score
        scored_hospitals.append(hospital_with_score)
    
    # Sort by AI score (descending) and then by rating
    scored_hospitals.sort(
        key=lambda x: (x['ai_score'], x['rating']), 
        reverse=True
    )
    
    return scored_hospitals

def get_hospital_recommendations(condition, location, max_results=10):
    """
    Get top hospital recommendations for a condition and location.
    
    Args:
        condition: Medical condition
        location: User location string
        max_results: Maximum number of results to return
    
    Returns:
        List of recommended hospitals with scores and explanations
    """
    # Default preferences for general recommendations
    hospital_types = ['Government', 'Private']
    min_rating = 3.0
    max_distance = 50
    
    matched_hospitals = match_hospitals_to_condition(
        condition, location, hospital_types, min_rating, max_distance
    )
    
    recommendations = []
    for hospital in matched_hospitals[:max_results]:
        recommendation = hospital.copy()
        
        # Add recommendation explanation
        explanation_parts = []
        
        if hospital.get('ai_score', 0) >= 80:
            explanation_parts.append("Excellent match for your condition")
        elif hospital.get('ai_score', 0) >= 60:
            explanation_parts.append("Good match for your condition")
        else:
            explanation_parts.append("Suitable for your condition")
        
        if hospital.get('nabh_accredited'):
            explanation_parts.append("NABH accredited facility")
        
        if hospital.get('emergency_services'):
            explanation_parts.append("24/7 emergency services available")
        
        if hospital['rating'] >= 4.5:
            explanation_parts.append("Highly rated by patients")
        
        recommendation['recommendation_reason'] = " • ".join(explanation_parts)
        recommendations.append(recommendation)
    
    return recommendations
