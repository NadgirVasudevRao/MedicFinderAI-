# Indian Hospital Finder 🏥

A comprehensive web application built with Streamlit that helps users find the best hospitals in India for their specific medical needs using AI-powered recommendations.

## Features

- **🔍 Smart Search**: Location-based hospital search with support for manual location input
- **🤖 AI-Powered Matching**: Intelligent hospital recommendations based on:
  - Specialty match with medical condition (40%)
  - Hospital quality and ratings (30%)
  - Accessibility factors (20%)
  - Distance from location (10%)
- **🗺️ Interactive Maps**: Visual hospital locations with detailed markers
- **⭐ Hospital Details**: Comprehensive information including:
  - Ratings and patient reviews
  - NABH accreditation status
  - Insurance acceptance
  - Emergency services availability
  - Detailed AI analysis breakdown
- **📱 Mobile Responsive**: Works seamlessly on both desktop and mobile devices

## Technology Stack

- **Frontend**: Streamlit
- **Mapping**: Folium with Streamlit-Folium integration
- **Geospatial**: Geopy for distance calculations and geocoding
- **Data Processing**: Pandas and NumPy
- **AI Matching**: Custom algorithm for hospital-condition matching

## Project Structure

```
indian-hospital-finder/
├── app.py                 # Main Streamlit application
├── data/
│   ├── conditions.py      # Medical conditions and specialty mappings
│   ├── hospitals.py       # Hospital database with details
│   └── locations.py       # Indian cities and coordinates
├── utils/
│   ├── ai_matcher.py      # AI-powered hospital matching algorithm
│   └── distance.py        # Distance calculation utilities
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/indian-hospital-finder.git
   cd indian-hospital-finder
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   Open your browser and go to `http://localhost:8501`

## Usage

1. **Select Location**
   - Choose your state and city from the dropdown menus
   - Or enter a specific location manually

2. **Choose Medical Condition**
   - Select condition category (Cardiovascular, Respiratory, etc.)
   - Pick specific condition from the list

3. **Set Preferences**
   - Hospital type (Government/Private)
   - Minimum rating requirement
   - Maximum search distance

4. **View Results**
   - Browse ranked hospital recommendations
   - View detailed AI analysis for each hospital
   - Explore interactive map with hospital locations
   - Access comprehensive hospital information

## AI Matching Algorithm

The AI scoring system evaluates hospitals based on:

### Specialty Matching (40%)
- Exact specialty matches for the medical condition
- Related specialty considerations
- Emergency condition prioritization

### Quality Assessment (30%)
- Hospital ratings and patient feedback
- NABH accreditation status
- Government hospital reliability factors

### Accessibility Factors (20%)
- Hospital type preferences
- 24/7 emergency services availability
- Insurance acceptance

### Distance Scoring (10%)
- Proximity to user location
- Travel time considerations

## Supported Medical Conditions

- **Cardiovascular**: Heart conditions, chest pain, hypertension
- **Respiratory**: Asthma, COPD, pneumonia, tuberculosis
- **Gastrointestinal**: Digestive issues, liver disease
- **Neurological**: Stroke, epilepsy, brain conditions
- **Orthopedic**: Bone fractures, joint problems, surgeries
- **Cancer/Oncology**: Various cancer types and treatments
- **Women's Health**: Pregnancy care, gynecological issues
- **Pediatric**: Children's healthcare needs
- **Emergency**: Trauma, accidents, critical conditions
- **And many more...**

## Coverage

The application covers major Indian cities across states including:
- Delhi, Mumbai, Bangalore, Chennai, Hyderabad
- Kolkata, Pune, Ahmedabad, Jaipur, Lucknow
- And 100+ other cities across India

## Hospital Database

Includes comprehensive information for:
- Government and private hospitals
- NABH accredited facilities
- Specialty hospitals and multi-specialty centers
- Emergency care providers
- Insurance-friendly hospitals

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Data Sources

- Hospital information compiled from verified healthcare directories
- Medical specialty mappings based on standard healthcare classifications
- Location data using OpenStreetMap and Nominatim geocoding

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is for informational purposes only. Always verify hospital information and consult with healthcare professionals for medical advice. The AI recommendations are suggestions based on available data and should not replace professional medical judgment.

## Support

For support or questions, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ for better healthcare accessibility in India**