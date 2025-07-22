import streamlit as st
import pandas as pd
import numpy as np
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium
from data.hospitals import HOSPITALS_DATA, get_hospitals_by_location
from data.locations import INDIAN_LOCATIONS, get_coordinates
from data.conditions import MEDICAL_CONDITIONS, get_condition_specialties
from utils.distance import calculate_distance
from utils.ai_matcher import match_hospitals_to_condition

# Page configuration
st.set_page_config(
    page_title="Indian Hospital Finder",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'selected_hospital' not in st.session_state:
    st.session_state.selected_hospital = None
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'search_performed' not in st.session_state:
    st.session_state.search_performed = False

# Main title and description
st.title("🏥 Hospital Finder")
st.markdown("Find the best hospitals in India for your medical needs with AI-powered recommendations")

# Sidebar for search inputs
st.sidebar.header("Search Parameters")

# Location input
st.sidebar.subheader("📍 Location")
selected_state = st.sidebar.selectbox(
    "Select State",
    options=list(INDIAN_LOCATIONS.keys()),
    index=0
)

selected_city = st.sidebar.selectbox(
    "Select City",
    options=INDIAN_LOCATIONS[selected_state],
    index=0
)

# Manual location input option
manual_location = st.sidebar.text_input(
    "Or enter location manually",
    placeholder="e.g., Sector 44, Gurgaon"
)

# Use manual location if provided, otherwise use selected city
search_location = manual_location if manual_location else f"{selected_city}, {selected_state}"

# Disease/Condition selection
st.sidebar.subheader("🩺 Medical Condition")
condition_category = st.sidebar.selectbox(
    "Condition Category",
    options=list(MEDICAL_CONDITIONS.keys())
)

specific_condition = st.sidebar.selectbox(
    "Specific Condition",
    options=MEDICAL_CONDITIONS[condition_category]
)

# Filter options
st.sidebar.subheader("🔍 Filters")
hospital_type = st.sidebar.multiselect(
    "Hospital Type",
    options=["Government", "Private"],
    default=["Government", "Private"]
)

min_rating = st.sidebar.slider(
    "Minimum Rating",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.5
)

max_distance = st.sidebar.slider(
    "Maximum Distance (km)",
    min_value=5,
    max_value=100,
    value=50,
    step=5
)

# Search button
search_clicked = st.sidebar.button("🔍 Search Hospitals", type="primary")

# Main content area
col1, col2 = st.columns([1, 1])

if search_clicked or st.session_state.search_results:
    if search_clicked:
        st.session_state.search_performed = True
        # Get user coordinates
        user_coords = get_coordinates(search_location)
        
        if user_coords:
            # Get relevant hospitals based on location and condition
            matched_hospitals = match_hospitals_to_condition(
                specific_condition, 
                search_location, 
                hospital_type,
                min_rating,
                max_distance
            )
            
            # Calculate distances and sort
            for hospital in matched_hospitals:
                hospital_coords = (hospital['latitude'], hospital['longitude'])
                distance = calculate_distance(user_coords, hospital_coords)
                hospital['distance'] = distance
            
            # Filter by distance and sort by AI score and rating
            filtered_hospitals = [h for h in matched_hospitals if h['distance'] <= max_distance]
            filtered_hospitals.sort(key=lambda x: (x.get('ai_score', 0), x['rating']), reverse=True)
            
            st.session_state.search_results = filtered_hospitals[:20]  # Top 20 results
        else:
            st.error("Could not find coordinates for the specified location. Please try a different location.")

    # Display results
    if st.session_state.search_results:
        with col1:
            st.subheader("🏥 Hospital Results")
            st.write(f"Found {len(st.session_state.search_results)} hospitals for **{specific_condition}** near **{search_location}**")
            
            # Display hospital cards
            for idx, hospital in enumerate(st.session_state.search_results):
                with st.container():
                    # Hospital card
                    card_container = st.container()
                    with card_container:
                        col_info, col_stats = st.columns([3, 1])
                        
                        with col_info:
                            st.write(f"**{hospital['name']}**")
                            st.write(f"📍 {hospital['address']}")
                            st.write(f"🏷️ {hospital['type']} • {hospital['specialties'][0] if hospital['specialties'] else 'General'}")
                            
                            if hospital.get('nabh_accredited'):
                                st.write("✅ NABH Accredited")
                            
                            if hospital.get('insurance_accepted'):
                                st.write(f"💳 Insurance: {', '.join(hospital['insurance_accepted'][:2])}")
                        
                        with col_stats:
                            st.metric("Rating", f"{hospital['rating']}/5")
                            st.metric("Distance", f"{hospital['distance']:.1f} km")
                            if hospital.get('ai_score'):
                                st.metric("AI Match", f"{hospital['ai_score']:.0f}%")
                                # Show underlying scores in a smaller format
                                if hospital.get('specialty_score') is not None:
                                    st.caption(f"🩺 Specialty: {hospital['specialty_score']:.0f}% • ⭐ Quality: {hospital['quality_score']:.0f}% • 🚗 Access: {hospital['accessibility_score']:.0f}%")
                    
                    # Select hospital button
                    if st.button(f"View Details", key=f"select_{idx}"):
                        st.session_state.selected_hospital = hospital
                        st.rerun()
                    
                    st.divider()
        
        with col2:
            st.subheader("🗺️ Map View")
            
            # Create map centered on user location or selected hospital
            if st.session_state.selected_hospital:
                center_lat = st.session_state.selected_hospital['latitude']
                center_lon = st.session_state.selected_hospital['longitude']
                zoom_level = 13
            else:
                user_coords = get_coordinates(search_location)
                if user_coords:
                    center_lat, center_lon = user_coords
                    zoom_level = 11
                else:
                    center_lat, center_lon = 28.6139, 77.2090  # Default to Delhi
                    zoom_level = 10
            
            # Create folium map
            m = folium.Map(
                location=[center_lat, center_lon],
                zoom_start=zoom_level,
                tiles="OpenStreetMap"
            )
            
            # Add user location marker
            user_coords = get_coordinates(search_location)
            if user_coords:
                folium.Marker(
                    user_coords,
                    popup=f"Your Location: {search_location}",
                    icon=folium.Icon(color='red', icon='user', prefix='fa')
                ).add_to(m)
            
            # Add hospital markers
            for hospital in st.session_state.search_results[:10]:  # Show top 10 on map
                color = 'green' if hospital.get('nabh_accredited') else 'blue'
                icon = 'plus' if hospital['type'] == 'Government' else 'hospital-o'
                
                popup_text = f"""
                <b>{hospital['name']}</b><br>
                Rating: {hospital['rating']}/5<br>
                Distance: {hospital['distance']:.1f} km<br>
                Type: {hospital['type']}
                """
                
                folium.Marker(
                    [hospital['latitude'], hospital['longitude']],
                    popup=popup_text,
                    icon=folium.Icon(color=color, icon=icon, prefix='fa')
                ).add_to(m)
            
            # Display map
            map_data = st_folium(m, width=500, height=400)

# Hospital details section
if st.session_state.selected_hospital:
    st.markdown("---")
    hospital = st.session_state.selected_hospital
    
    st.subheader(f"🏥 {hospital['name']}")
    
    # Hospital info tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["ℹ️ Details", "🤖 AI Analysis", "⭐ Reviews", "📞 Contact", "🗺️ Directions"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Basic Information**")
            st.write(f"**Type:** {hospital['type']}")
            st.write(f"**Rating:** {hospital['rating']}/5")
            st.write(f"**Distance:** {hospital['distance']:.1f} km")
            
            if hospital.get('nabh_accredited'):
                st.success("✅ NABH Accredited")
            
            if hospital.get('emergency_services'):
                st.info("🚨 24/7 Emergency Services")
        
        with col2:
            st.write("**Specialties**")
            for specialty in hospital['specialties']:
                st.write(f"• {specialty}")
        
        with col3:
            st.write("**Insurance Accepted**")
            if hospital.get('insurance_accepted'):
                for insurance in hospital['insurance_accepted']:
                    st.write(f"• {insurance}")
            else:
                st.write("Please contact hospital for insurance details")
    
    with tab2:
        st.write("**AI Matching Analysis**")
        
        if hospital.get('ai_score'):
            # Overall AI Score
            col1, col2 = st.columns([1, 3])
            with col1:
                st.metric("Overall AI Match", f"{hospital['ai_score']:.0f}%")
            with col2:
                if hospital['ai_score'] >= 80:
                    st.success("🎯 Excellent match for your medical condition")
                elif hospital['ai_score'] >= 60:
                    st.info("✅ Good match for your medical condition")
                else:
                    st.warning("⚠️ Basic match - suitable but not specialized")
            
            st.divider()
            
            # Component Scores Breakdown
            col1, col2, col3, col4 = st.columns(4)
            
            if hospital.get('specialty_score') is not None:
                with col1:
                    st.metric("🩺 Specialty Match", f"{hospital['specialty_score']:.0f}%")
                    st.caption("How well hospital specialties match your condition")
            
            if hospital.get('quality_score') is not None:
                with col2:
                    st.metric("⭐ Quality Score", f"{hospital['quality_score']:.0f}%")
                    st.caption("Rating, accreditation, and facility standards")
            
            if hospital.get('accessibility_score') is not None:
                with col3:
                    st.metric("🚗 Accessibility", f"{hospital['accessibility_score']:.0f}%")
                    st.caption("Type preference, emergency services, insurance")
            
            if hospital.get('distance_score') is not None:
                with col4:
                    st.metric("📍 Distance Score", f"{hospital['distance_score']:.0f}%")
                    st.caption("Proximity to your location")
            
            st.divider()
            
            # Detailed explanation
            st.write("**Why this hospital was recommended:**")
            reasons = []
            
            if hospital.get('specialty_score', 0) >= 70:
                reasons.append("✅ Has specialized departments for your medical condition")
            elif hospital.get('specialty_score', 0) >= 40:
                reasons.append("⚠️ Has related specialties that can treat your condition")
            else:
                reasons.append("ℹ️ General hospital that provides basic care for your condition")
            
            if hospital.get('nabh_accredited'):
                reasons.append("✅ NABH accredited - meets national quality standards")
            
            if hospital['rating'] >= 4.5:
                reasons.append("✅ Highly rated by patients")
            elif hospital['rating'] >= 4.0:
                reasons.append("✅ Good patient ratings")
            
            if hospital.get('emergency_services'):
                reasons.append("✅ 24/7 emergency services available")
            
            if hospital.get('distance', 0) <= 10:
                reasons.append("✅ Close to your location")
            elif hospital.get('distance', 0) <= 25:
                reasons.append("ℹ️ Reasonable distance from your location")
            
            for reason in reasons:
                st.write(f"• {reason}")
        else:
            st.info("AI analysis not available for this hospital")
    
    with tab3:
        st.write("**Top 5 Patient Reviews**")
        
        # Mock reviews for the selected hospital
        reviews = [
            {
                "rating": 5,
                "text": "Excellent care and professional staff. The doctors were very knowledgeable and the facilities are modern.",
                "author": "Rajesh K.",
                "date": "2024-01-15"
            },
            {
                "rating": 4,
                "text": "Good hospital with quality treatment. Wait time could be better but overall satisfied.",
                "author": "Priya S.",
                "date": "2024-01-10"
            },
            {
                "rating": 5,
                "text": "Outstanding service during emergency. Quick response and excellent medical care.",
                "author": "Mohammed A.",
                "date": "2024-01-08"
            },
            {
                "rating": 4,
                "text": "Clean facilities and experienced doctors. Billing was transparent and reasonable.",
                "author": "Lakshmi R.",
                "date": "2024-01-05"
            },
            {
                "rating": 3,
                "text": "Decent hospital but can be crowded. Staff is helpful and treatment quality is good.",
                "author": "Amit P.",
                "date": "2024-01-02"
            }
        ]
        
        for review in reviews:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"⭐ **{review['rating']}/5** - {review['author']}")
                    st.write(review['text'])
                with col2:
                    st.write(review['date'])
                st.divider()
    
    with tab4:
        st.write("**Contact Information**")
        st.write(f"**Address:** {hospital['address']}")
        st.write(f"**Phone:** {hospital.get('phone', '+91-XXX-XXX-XXXX')}")
        st.write(f"**Email:** {hospital.get('email', 'info@hospital.com')}")
        
        if hospital.get('website'):
            st.write(f"**Website:** {hospital['website']}")
        
        st.write("**Operating Hours:**")
        st.write("• OPD: 9:00 AM - 6:00 PM")
        st.write("• Emergency: 24/7")
    
    with tab5:
        st.write("**Directions**")
        user_coords = get_coordinates(search_location)
        if user_coords:
            st.write(f"**From:** {search_location}")
            st.write(f"**To:** {hospital['name']}")
            st.write(f"**Distance:** {hospital['distance']:.1f} km")
            
            # Simple directions (in a real app, you'd use a routing API)
            st.info("🚗 Use Google Maps or similar navigation app for detailed turn-by-turn directions")
            
            # Show coordinates for manual navigation
            st.write(f"**Hospital Coordinates:** {hospital['latitude']}, {hospital['longitude']}")
        
        # Back to search button
        if st.button("🔙 Back to Search Results"):
            st.session_state.selected_hospital = None
            st.rerun()

elif not st.session_state.search_performed:
    # Welcome screen - only show if no search has been performed
    st.markdown("""
    ## Welcome to Indian Hospital Finder 🏥
    
    Find the best hospitals in India for your medical needs with our AI-powered recommendation system.
    
    ### Features:
    - 🔍 Search hospitals by location and medical condition
    - 🤖 AI-powered hospital matching based on specialties
    - ⭐ Hospital ratings and patient reviews
    - 🗺️ Interactive maps with hospital locations
    - 🏥 Government and private hospital options
    - ✅ NABH accreditation status
    - 💳 Insurance acceptance information
    
    ### How to use:
    1. Select your state and city from the sidebar
    2. Choose your medical condition
    3. Set your preferences (hospital type, rating, distance)
    4. Click "Search Hospitals" to find recommendations
    5. View detailed information and reviews
    
    **Get started by filling in your search criteria in the sidebar!**
    """)
