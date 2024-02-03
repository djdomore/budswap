import streamlit as st

# Sample Product Data
products = [
    {"name": "Product 1", "price": 29.99, "description": "Description of Product 1"},
    {"name": "Product 2", "price": 49.99, "description": "Description of Product 2"},
    {"name": "Product 3", "price": 19.99, "description": "Description of Product 3"},
]

# Function to display product details
def display_product(product):
    st.write(f"**{product['name']}**")
    st.write(f"Price: ${product['price']}")
    st.write(f"Description: {product['description']}")
    st.write("---")

# Main App
def main():
    st.title("E-Commerce Marketplace")

    # Display product listings
    st.header("Product Listings")
    for product in products:
        display_product(product)

    # Product details based on user selection
    selected_product = st.selectbox("Select a Product", products, format_func=lambda product: product["name"])
    st.subheader("Selected Product Details:")
    display_product(selected_product)

    # Shopping Cart
    st.header("Shopping Cart")
    cart = st.session_state.get("cart", [])

    if st.button("Add to Cart"):
        cart.append(selected_product)
        st.session_state.cart = cart
        st.success(f"{selected_product['name']} added to the cart!")

    # Display Shopping Cart
    if cart:
        st.subheader("Your Shopping Cart:")
        for item in cart:
            display_product(item)
    else:
        st.info("Your cart is empty.")

if __name__ == "__main__":
    main()
