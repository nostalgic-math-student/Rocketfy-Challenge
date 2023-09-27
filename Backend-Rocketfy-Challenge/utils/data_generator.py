import json
import random
import string

# Function to generate a random product name
def generate_random_product_name():
    adjectives = ["Amazing", "Awesome", "Good-looking", "Top-notch", "High-end", "Classic"]
    nouns = ["Shirt", "Skirt", "Hat", "Jeans", "Jacket", "Dress"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

# Function to generate a random SKU (Stock Keeping Unit)
def generate_random_sku():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Function to generate a random product description based on the product name
def generate_random_description(product_name):
    return f"This {product_name} is a lovely item that you'll adore!"



# Function to generate a list of product records
def generate_clothing_records(num_records, image_paths):
    records = []
    for _ in range(num_records):
        product_name = generate_random_product_name()
        sku = generate_random_sku()
        description = generate_random_description(product_name)
        img_url = random.choice(image_paths)  # Choose a random image URL
        record = {"name": product_name, "SKU": sku, "description": description, "img_url": img_url, "category":"clothing"}
        records.append(record)
    return records

## Tech products

def generate_random_techproduct_name():
    adjectives = ["Web3", "VR", "High-end", "Gamer", "Minimalist", "XL"]
    nouns = ["SmartWatch", "Headphones", "PC", "Monitor", "Headset", "Keyboard"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def generate_tech_records(num_records, image_paths):
    records = []
    for _ in range(num_records):
        product_name = generate_random_techproduct_name()
        sku = generate_random_sku()
        description = generate_random_description(product_name)
        img_url = random.choice(image_paths)  # Choose a random image URL
        record = {"name": product_name, "SKU": sku, "description": description, "img_url": img_url, "category":"tech"}
        records.append(record)
    return records

# Function to create a JSON file with the specified number of records
def create_json_file(filename, num_records, image_path1, image_path2):
    record1 = generate_clothing_records(num_records, image_path1)
    record2 = generate_tech_records(num_records, image_path2)

    records = []
    records.extend(record1)
    records.extend(record2)

    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

# list of random pictures for product description
image_paths1 = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png"]
image_paths2 = ["img6.png", "img7.png", "img8.png", "img9.png", "img10.png"]
# Dummy information created
create_json_file("product_records.json", 150, image_paths1, image_paths2)