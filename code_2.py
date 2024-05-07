#content-based filtering project 



import streamlit as st
from fuzzywuzzy import process

# Sample product database
product_data = {
    "Toothpaste": ["Colgate Total", "Sensodyne", "clinica"],
    "Shampoo": ["Head & Shoulders", "Pantene Pro-V", "Herbal Essences"],
    "Soap": ["Dove Beauty Bar", "Lux soap", "Care beauty soap "],
    "Moisturizer": ["Cetaphil Moisturizing Cream", "Aveeno Daily Moisturizing Lotion", "Nivea Soft Moisturizing Creme"],
    "Deodorant": ["Degree Men's Dry Protection", "Secret Clinical Strength", "Dove Advanced Care Antiperspirant"],
    "Laundry Detergent": ["Tide Original", "Persil ProClean", "Seventh Generation Free & Clear"],
    "Dish Soap": ["Dawn Ultra", "Palmolive Ultra Strength", "Mrs. Meyer's Clean Day Dish Soap"],
    "Hand Sanitizer": ["Purell Advanced Hand Sanitizer", "Germ-X Hand Sanitizer", "EO Hand Sanitizer"],
    "Lip Balm": ["Burt's Bees Beeswax Lip Balm", "Carmex Classic Lip Balm", "Aquaphor Lip Repair"],
    "Sunscreen": ["Neutrogena Ultra Sheer Dry-Touch Sunscreen", "Banana Boat Ultra Sport Sunscreen", "Coppertone Sport Sunscreen Spray"],
    "Facial Cleanser": ["Cetaphil Gentle Skin Cleanser", "Neutrogena Oil-Free Acne Wash", "La Roche-Posay Toleriane Hydrating Gentle Cleanser"],
    "Toilet Paper": ["Charmin Ultra Soft", "Cottonelle Ultra ComfortCare", "Scott 1000 Sheets Per Roll"],
    "Tissues": ["Kleenex Facial Tissues", "Puffs Plus Lotion Facial Tissues", "Seventh Generation Facial Tissues"],
    "Hand Cream": ["L'Occitane Shea Butter Hand Cream", "Aveeno Skin Relief Hand Cream", "Eucerin Advanced Repair Hand Cream"],
    "Razors": ["Gillette Mach3 Men's Razor", "Schick Hydro Silk Women's Razor", "Harry's Men's Razor"],
    "Coffee": ["Folgers Classic Roast", "Starbucks Pike Place Roast", "Dunkin' Donuts Original Blend"],
    "Tea": ["Mezban Tea", "Tapal Danedar", "Lipton Black Tea"],
    "Cooking Oil": ["Bertolli Extra Virgin Olive Oil", "Crisco Pure Vegetable Oil", "Spectrum Organic Coconut Oil"],
    "Toothbrush": ["Oral-B Pro-Health Clinical Battery Powered Toothbrush", "Colgate 360 Total Advanced Floss-Tip Bristles Toothbrush", "Philips Sonicare ProtectiveClean 4100 Electric Toothbrush"],
    "Hand Soap": ["Softsoap Liquid Hand Soap", "Method Gel Hand Soap", "Mrs. Meyer's Clean Day Hand Soap"],
    "Cereal": ["Cheerios", "Special K", "Honey Bunches of Oats"],
    "Bread": ["Wonder Bread", "Dave's Killer Bread", "Pepperidge Farm Farmhouse Bread"],
    "Milk": ["Organic Valley Whole Milk", "Horizon Organic 2% Milk", "Silk Almond Milk"],
    "Peanut Butter": ["Jif Creamy Peanut Butter", "Skippy Creamy Peanut Butter", "Justin's Classic Peanut Butter"],
    "Jam/Jelly": ["Smucker's Strawberry Jam", "Welch's Grape Jelly", "Bonne Maman Raspberry Preserves"],
    "Cheese": ["Kraft Cheddar Cheese", "Tillamook Medium Cheddar Cheese", "Cabot Extra Sharp Cheddar Cheese"],
    "Eggs": ["Organic Valley Large Brown Eggs", "Eggland's Best Large Eggs", "Vital Farms Pasture-Raised Large Eggs"],
    "Yogurt": ["Chobani Greek Yogurt", "Fage Total Greek Yogurt", "Siggi's Icelandic Style Yogurt"],
    "Granola Bars": ["Nature Valley Crunchy Granola Bars", "KIND Bars", "Clif Bars"],
    "Bottled Water": ["Nastle", "Aquafina", "atlantic mineral water"]
}

def get_recommendations(product_name):
    # Use FuzzyWuzzy to find the closest match for the user input
    match, score = process.extractOne(product_name, product_data.keys())
    return product_data.get(match, [])

# Streamlit UI
st.title("Product Recommendation System")

# User input for product search
search_product = st.text_input("Search for a product:")

# Generate recommendations based on search box input
if search_product:
    recommended_products = get_recommendations(search_product)
    if recommended_products:
        st.write(f"Top Recommended products for {search_product}:")
        for i, product in enumerate(recommended_products, start=1):
            st.write(f"{i}. {product}")
    else:
        st.write("No recommendations found for the specified product.")




