import random

PHONE_VARIANTS = ["128GB", "256GB", "512GB"]
LAPTOP_VARIANTS = ["16GB RAM", "32GB RAM"]
WATCH_VARIANTS = ["44mm", "46mm"]
DEFAULT_VARIANTS = [""]

PRICE_INCREMENT = {
    "128GB": 0,
    "256GB": 10000,
    "512GB": 25000,
    "16GB RAM": 0,
    "32GB RAM": 20000,
    "44mm": 0,
    "46mm": 5000,
    "": 0
}


def get_variants(category):

    if category == "Smartphone":
        return PHONE_VARIANTS

    if category == "Laptop":
        return LAPTOP_VARIANTS

    if category == "Watch":
        return WATCH_VARIANTS

    return DEFAULT_VARIANTS


def generate_sku(brand, product_name, variant):

    brand_code = brand[:3].upper()

    product_code = "".join(
        word[:2].upper()
        for word in product_name.split()
    )

    variant_code = (
        variant.replace("GB", "")
        .replace("RAM", "")
        .replace("mm", "")
        .replace(" ", "")
    )

    if variant_code:
        return f"{brand_code}-{product_code}-{variant_code}"

    return f"{brand_code}-{product_code}"


def generate_stock():

    return random.randint(30, 500)