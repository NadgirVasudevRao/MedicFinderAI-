"""
Medical conditions and specialties common in Indian healthcare context.
Organized by categories with mapping to hospital specialties.
"""

MEDICAL_CONDITIONS = {
    "Cardiovascular": [
        "Heart Attack (Myocardial Infarction)",
        "Chest Pain",
        "High Blood Pressure (Hypertension)",
        "Heart Failure",
        "Arrhythmia",
        "Coronary Artery Disease",
        "Valve Disease",
        "Congenital Heart Disease",
        "Peripheral Artery Disease"
    ],
    
    "Respiratory": [
        "Asthma",
        "COPD (Chronic Obstructive Pulmonary Disease)",
        "Pneumonia",
        "Tuberculosis (TB)",
        "Lung Cancer",
        "Respiratory Infections",
        "Sleep Apnea",
        "Pulmonary Embolism",
        "Bronchitis"
    ],
    
    "Gastrointestinal": [
        "Stomach Pain",
        "Acid Reflux (GERD)",
        "Liver Disease",
        "Hepatitis",
        "Gallstones",
        "Inflammatory Bowel Disease",
        "Peptic Ulcer",
        "Colorectal Cancer",
        "Pancreatitis"
    ],
    
    "Neurological": [
        "Stroke",
        "Epilepsy",
        "Migraine",
        "Parkinson's Disease",
        "Alzheimer's Disease",
        "Multiple Sclerosis",
        "Brain Tumor",
        "Spinal Cord Injury",
        "Neuropathy"
    ],
    
    "Orthopedic": [
        "Bone Fractures",
        "Joint Pain",
        "Arthritis",
        "Back Pain",
        "Sports Injuries",
        "Hip Replacement",
        "Knee Replacement",
        "Osteoporosis",
        "Spine Disorders"
    ],
    
    "Cancer/Oncology": [
        "Breast Cancer",
        "Lung Cancer",
        "Colorectal Cancer",
        "Prostate Cancer",
        "Cervical Cancer",
        "Leukemia",
        "Lymphoma",
        "Liver Cancer",
        "Oral Cancer"
    ],
    
    "Women's Health": [
        "Pregnancy Care",
        "High-Risk Pregnancy",
        "Gynecological Issues",
        "Menstrual Disorders",
        "PCOS (Polycystic Ovary Syndrome)",
        "Infertility Treatment",
        "Menopause",
        "Breast Disorders",
        "Cervical Screening"
    ],
    
    "Pediatric": [
        "Childhood Fever",
        "Vaccination",
        "Growth Disorders",
        "Childhood Asthma",
        "Developmental Delays",
        "Pediatric Surgery",
        "Neonatal Care",
        "Childhood Infections",
        "Congenital Disorders"
    ],
    
    "Endocrine": [
        "Diabetes Type 1",
        "Diabetes Type 2",
        "Thyroid Disorders",
        "Obesity",
        "Hormonal Disorders",
        "Adrenal Disorders",
        "Metabolic Syndrome",
        "Growth Hormone Disorders"
    ],
    
    "Kidney/Urology": [
        "Kidney Stones",
        "Chronic Kidney Disease",
        "Urinary Tract Infections",
        "Prostate Problems",
        "Kidney Transplant",
        "Dialysis",
        "Bladder Issues",
        "Male Infertility"
    ],
    
    "Mental Health": [
        "Depression",
        "Anxiety Disorders",
        "Bipolar Disorder",
        "Schizophrenia",
        "PTSD",
        "Substance Abuse",
        "Eating Disorders",
        "Sleep Disorders",
        "Stress Management"
    ],
    
    "Emergency": [
        "Accident/Trauma",
        "Poisoning",
        "Severe Burns",
        "Heart Attack",
        "Stroke",
        "Severe Bleeding",
        "Difficulty Breathing",
        "Loss of Consciousness",
        "Severe Pain"
    ]
}

# Mapping conditions to hospital specialties
CONDITION_TO_SPECIALTY = {
    # Cardiovascular
    "heart attack": ["Cardiology", "Emergency Medicine"],
    "chest pain": ["Cardiology", "Emergency Medicine"],
    "hypertension": ["Cardiology", "Internal Medicine"],
    "heart failure": ["Cardiology"],
    "arrhythmia": ["Cardiology"],
    "coronary artery disease": ["Cardiology", "Cardiac Surgery"],
    "valve disease": ["Cardiology", "Cardiac Surgery"],
    "congenital heart disease": ["Cardiology", "Pediatric Cardiology"],
    
    # Respiratory
    "asthma": ["Pulmonology", "Allergy"],
    "copd": ["Pulmonology"],
    "pneumonia": ["Pulmonology", "Internal Medicine"],
    "tuberculosis": ["Pulmonology", "Infectious Disease"],
    "lung cancer": ["Oncology", "Pulmonology", "Thoracic Surgery"],
    "respiratory infections": ["Pulmonology", "Internal Medicine"],
    
    # Gastrointestinal
    "stomach pain": ["Gastroenterology", "Internal Medicine"],
    "acid reflux": ["Gastroenterology"],
    "liver disease": ["Gastroenterology", "Hepatology"],
    "hepatitis": ["Gastroenterology", "Hepatology"],
    "gallstones": ["Gastroenterology", "General Surgery"],
    "inflammatory bowel disease": ["Gastroenterology"],
    "peptic ulcer": ["Gastroenterology"],
    "colorectal cancer": ["Oncology", "Gastroenterology", "General Surgery"],
    
    # Neurological
    "stroke": ["Neurology", "Emergency Medicine"],
    "epilepsy": ["Neurology"],
    "migraine": ["Neurology"],
    "parkinson's disease": ["Neurology"],
    "alzheimer's disease": ["Neurology", "Geriatrics"],
    "brain tumor": ["Neurology", "Neurosurgery", "Oncology"],
    "spinal cord injury": ["Neurology", "Neurosurgery", "Rehabilitation"],
    
    # Orthopedic
    "bone fractures": ["Orthopedics", "Emergency Medicine"],
    "joint pain": ["Orthopedics", "Rheumatology"],
    "arthritis": ["Orthopedics", "Rheumatology"],
    "back pain": ["Orthopedics", "Neurology"],
    "sports injuries": ["Orthopedics", "Sports Medicine"],
    "hip replacement": ["Orthopedics"],
    "knee replacement": ["Orthopedics"],
    
    # Cancer/Oncology
    "breast cancer": ["Oncology", "Surgical Oncology"],
    "prostate cancer": ["Oncology", "Urology"],
    "cervical cancer": ["Oncology", "Gynecology"],
    "leukemia": ["Oncology", "Hematology"],
    "lymphoma": ["Oncology", "Hematology"],
    
    # Women's Health
    "pregnancy care": ["Obstetrics", "Gynecology"],
    "high-risk pregnancy": ["Maternal Fetal Medicine", "Obstetrics"],
    "gynecological issues": ["Gynecology"],
    "pcos": ["Gynecology", "Endocrinology"],
    "infertility treatment": ["Reproductive Medicine", "Gynecology"],
    
    # Pediatric
    "childhood fever": ["Pediatrics"],
    "vaccination": ["Pediatrics"],
    "growth disorders": ["Pediatrics", "Endocrinology"],
    "childhood asthma": ["Pediatrics", "Pulmonology"],
    "pediatric surgery": ["Pediatric Surgery"],
    
    # Endocrine
    "diabetes type 1": ["Endocrinology"],
    "diabetes type 2": ["Endocrinology", "Internal Medicine"],
    "thyroid disorders": ["Endocrinology"],
    "obesity": ["Endocrinology", "Bariatric Surgery"],
    
    # Kidney/Urology
    "kidney stones": ["Urology", "Nephrology"],
    "chronic kidney disease": ["Nephrology"],
    "urinary tract infections": ["Urology", "Internal Medicine"],
    "prostate problems": ["Urology"],
    "kidney transplant": ["Nephrology", "Transplant Surgery"],
    
    # Mental Health
    "depression": ["Psychiatry", "Psychology"],
    "anxiety disorders": ["Psychiatry", "Psychology"],
    "bipolar disorder": ["Psychiatry"],
    "schizophrenia": ["Psychiatry"],
    
    # Emergency
    "accident": ["Emergency Medicine", "Trauma Surgery"],
    "trauma": ["Emergency Medicine", "Trauma Surgery"],
    "severe burns": ["Emergency Medicine", "Plastic Surgery"],
    "severe bleeding": ["Emergency Medicine", "General Surgery"]
}

def get_condition_specialties(condition):
    """Get relevant medical specialties for a given condition"""
    condition_lower = condition.lower()
    
    # Look for exact matches first
    if condition_lower in CONDITION_TO_SPECIALTY:
        return CONDITION_TO_SPECIALTY[condition_lower]
    
    # Look for partial matches
    specialties = []
    for key, specs in CONDITION_TO_SPECIALTY.items():
        if any(word in condition_lower for word in key.split()):
            specialties.extend(specs)
    
    # Remove duplicates and return
    return list(set(specialties)) if specialties else ["General Medicine"]

def get_conditions_by_specialty(specialty):
    """Get conditions that can be treated by a given specialty"""
    conditions = []
    specialty_lower = specialty.lower()
    
    for condition, specialties in CONDITION_TO_SPECIALTY.items():
        if any(specialty_lower in spec.lower() for spec in specialties):
            conditions.append(condition.title())
    
    return conditions

def is_emergency_condition(condition):
    """Check if a condition requires emergency care"""
    emergency_keywords = [
        "heart attack", "stroke", "severe", "emergency", "trauma", 
        "accident", "bleeding", "poisoning", "burns", "difficulty breathing",
        "loss of consciousness", "chest pain"
    ]
    
    condition_lower = condition.lower()
    return any(keyword in condition_lower for keyword in emergency_keywords)
