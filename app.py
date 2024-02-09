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
import streamlit as st
import pandas as pd

# Title of the application
st.title("BudSwap - Plant & Seed Exchange")

# Initialize an empty dataframe to store the listings
# In a production app, this would be replaced by a persistent database
listings = pd.DataFrame(columns=["Name", "Have", "Want", "Contact"])

# Function to add a new listing to the dataframe
def add_listing(name, have, want, contact):
    global listings
    new_entry = {"Name": name, "Have": have, "Want": want, "Contact": contact}
    listings = listings.append(new_entry, ignore_index=True)

# Check if the listings dataframe should be loaded from the session state
if 'listings' in st.session_state:
    listings = st.session_state['listings']

# Form for users to enter their listing
with st.form("new_listing"):
    st.subheader("Create a New Listing")
    name = st.text_input("Your Name")
    have = st.text_input("What do you have to swap? (e.g., plant, seeds)")
    want = st.text_input("What are you looking for?")
    contact = st.text_input("Contact Information (e.g., email)")
    
    submitted = st.form_submit_button("Submit Listing")
    if submitted:
        add_listing(name, have, want, contact)
        st.session_state['listings'] = listings  # Save to session state
        st.success("Your listing has been added!")

# Display current listings
st.subheader("Current Listings")
st.table(listings)

# Run the Streamlit app by pasting the code into a Python script and
# using the command: streamlit run yourscript.py
