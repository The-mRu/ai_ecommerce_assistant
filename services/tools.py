from database.mongodb import (
    get_product_by_name,
    get_reviews_by_product,
    recommend_products,
    search_products
)


# =========================
# SEARCH PRODUCTS TOOL
# =========================

def search_products_tool(query):

    products = search_products(query)

    if not products:

        return "No matching products found."

    lines = []

    for product in products:

        lines.append(

            f"{product['name']} "
            f"(${product['price']}) "
            f"- {product['sub_category']}"
        )

    return "\n".join(lines)


# =========================
# REVIEW SUMMARY
# =========================

def summarize_reviews_tool(product_name):

    reviews = get_reviews_by_product(product_name)

    if not reviews:

        return "No reviews found."

    # Prioritize latest reviews
    latest_reviews = reviews[:5]

    combined_reviews = "\n".join(

        [
            review["review"]
            for review in latest_reviews
        ]
    )

    return combined_reviews


# =========================
# COMPARE PRODUCTS TOOL
# =========================

def compare_products_tool(products):

    found_products = []

    for name in products:

        product = get_product_by_name(name)

        if product:

            found_products.append(product)

    if len(found_products) < 2:

        return "Need at least 2 valid products to compare."

    comparison = []

    for product in found_products:

        comparison.append(

            f"""
            Name: {product['name']}
            Price: ${product['price']}
            Battery: {product['battery']}
            Camera: {product['camera']}
            Gaming: {product['gaming']}
            Rating: {product['rating']}
            """
        )

    return "\n".join(comparison)


# =========================
# RECOMMEND PRODUCTS TOOL
# =========================

def recommend_products_tool(category=None, max_price=None):

    products = recommend_products(

        category=category,

        max_price=max_price
    )

    if not products:

        return "No matching products found."

    lines = []

    for product in products[:5]:

        lines.append(

            f"{product['name']} "
            f"(${product['price']})"
        )

    return "\n".join(lines)