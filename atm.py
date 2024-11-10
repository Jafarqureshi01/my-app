import streamlit as st

# ATM class definition
class ATM:
    def __init__(self, pin_generate, initial_balance=0):
        self.pin_generate = pin_generate
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            return f"Deposited: {amount}. New Balance: {self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            return f"Withdrew: {amount}. New Balance: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def check_balance(self):
        return f"Current Balance: {self.balance}"

    def view_transaction_history(self):
        return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."

# Streamlit interface
def main():
    st.title("ATM System")

    # Session state for storing pin and ATM instance
    if "atm" not in st.session_state:
        st.session_state["atm"] = None

    if st.session_state["atm"] is None:
        # Initial setup - User enters PIN and initial balance
        pin_generate = st.text_input("Enter your PIN", type="password")
        initial_balance = st.number_input("Enter your initial balance", min_value=0, value=0)

        # Create ATM object when user provides PIN and initial balance
        if st.button("Setup ATM"):
            if pin_generate and initial_balance >= 0:
                st.session_state["atm"] = ATM(pin_generate, initial_balance)
                st.success(f"ATM setup successful! Initial Balance: {initial_balance}")
            else:
                st.error("Please enter a valid PIN and initial balance.")

    else:
        # User has already set up ATM
        atm = st.session_state["atm"]
        st.subheader("Welcome to Your ATM")

        menu = ["Deposit", "Withdraw", "Check Balance", "View Transaction History", "Exit"]
        choice = st.radio("Choose an action", menu)

        if choice == "Deposit":
            deposit_amount = st.number_input("Enter amount to deposit", min_value=0)
            if st.button("Deposit"):
                result = atm.deposit(deposit_amount)
                st.success(result)

        elif choice == "Withdraw":
            withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0)
            if st.button("Withdraw"):
                result = atm.withdraw(withdraw_amount)
                st.success(result)

        elif choice == "Check Balance":
            result = atm.check_balance()
            st.write(result)

        elif choice == "View Transaction History":
            transaction_history = atm.view_transaction_history()
            st.text_area("Transaction History", value=transaction_history, height=200)

        elif choice == "Exit":
            st.session_state["atm"] = None
            st.success("Thank you for using the ATM. You have logged out.")

# Run the app
if __name__ == "__main__":
    main()
