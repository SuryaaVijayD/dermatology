import googletrans

translator = googletrans.Translator()

d = {
    "DiseaseName": "Acne",
    "Tips": [
        "Eating a healthy diet that is rich in fruits, vegetables, and whole grains.",
        "Limiting processed foods, sugary drinks, and unhealthy fats.",
        "Drinking plenty of water.",
        "Eating foods that are high in omega-3 fatty acids, such as fish, flaxseeds, and walnuts.",
        "Avoiding foods that are high in dairy and refined carbohydrates.",
    ],
    "FoodsToTake": ["Fruits and vegetables", "Whole grains", "Omega-3 fatty acids"],
    "FoodsNotToTake": ["Dairy products", "Refined carbohydrates", "Processed foods"],
    "Doctors": [
        {
            "Dermatologist_ID": 7,
            "Name": "Dr. S. Patel",
            "Specialization": "Acne",
            "Location": "Bangalore",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 94,
            "Name": "Dr. R. Nair",
            "Specialization": "Acne",
            "Location": "Hyderabad",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 16,
            "Name": "Dr. A. Sharma",
            "Specialization": "Acne",
            "Location": "Chennai",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 79,
            "Name": "Dr. S. Menon",
            "Specialization": "Acne",
            "Location": "Chennai",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 25,
            "Name": "Dr. A. Srinivasan",
            "Specialization": "Acne",
            "Location": "Hyderabad",
            "Patient_Rating": 4.9,
        },
    ],
    "Warning": [],
}
{
    "DiseaseName": "Acne",
    "Tips": [
        "Eating a healthy diet that is rich in fruits, vegetables, and whole grains.",
        "Limiting processed foods, sugary drinks, and unhealthy fats.",
        "Drinking plenty of water.",
        "Eating foods that are high in omega-3 fatty acids, such as fish, flaxseeds, and walnuts.",
        "Avoiding foods that are high in dairy and refined carbohydrates.",
    ],
    "FoodsToTake": ["Fruits and vegetables", "Whole grains", "Omega-3 fatty acids"],
    "FoodsNotToTake": ["Dairy products", "Refined carbohydrates", "Processed foods"],
    "Doctors": [
        {
            "Dermatologist_ID": 7,
            "Name": "Dr. S. Patel",
            "Specialization": "Acne",
            "Location": "Bangalore",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 94,
            "Name": "Dr. R. Nair",
            "Specialization": "Acne",
            "Location": "Hyderabad",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 16,
            "Name": "Dr. A. Sharma",
            "Specialization": "Acne",
            "Location": "Chennai",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 79,
            "Name": "Dr. S. Menon",
            "Specialization": "Acne",
            "Location": "Chennai",
            "Patient_Rating": 4.9,
        },
        {
            "Dermatologist_ID": 25,
            "Name": "Dr. A. Srinivasan",
            "Specialization": "Acne",
            "Location": "Hyderabad",
            "Patient_Rating": 4.9,
        },
    ],
    "Warning": [],
}

text = translator.translate(d, 'ta')

print(text.text)
