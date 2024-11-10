import streamlit as st

# Define the menu of restaurant
menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80,
}

# Streamlit interface
def main():
    st.title("Welcome to Balaji Restaurant")
    st.write("Here is the menu:")

    # Display the menu items and prices
    for item, price in menu.items():
        st.write(f"{item.capitalize()}: Rs {price}")

    # Initialize order total and ordered items in session state if not already
    if "order_total" not in st.session_state:
        st.session_state["order_total"] = 0
        st.session_state["ordered_items"] = []

    # Start the ordering process
    st.subheader("Your Order")

    # Select items from the menu
    order_item = st.selectbox("Choose an item to order:", list(menu.keys()))

    # Add the selected item to the order if the item exists in the menu
    if order_item:
        st.session_state["order_total"] += menu[order_item]
        st.session_state["ordered_items"].append(order_item)
        st.success(f"You added {order_item} to your order. Total so far: Rs {st.session_state['order_total']}")

    # Allow user to add more items using a button instead of 'rerun'
    add_another_item = st.button("Add another item")

    # Check if user wants to add more items
    if add_another_item:
        # Nothing to do, as the button will trigger re-rendering of the page
        st.experimental_rerun()  # Only if you want to trigger a full app rerun

    # Display the ordered items and the final total bill
    if st.session_state["ordered_items"]:
        st.subheader("Your Order Summary:")
        for item in st.session_state["ordered_items"]:
            st.write(f"- {item.capitalize()}")
        
        st.subheader(f"Your total bill is Rs {st.session_state['order_total']}")
    
    # Thank the customer for dining with us
    st.write("Thank you for dining with us!")

# Run the app
if __name__ == "__main__":
    main()
