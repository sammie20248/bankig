💻 ELITE BANK - Streamlit Banking App

A simple banking application built with Python and Streamlit that simulates savings and current accounts with basic deposit, withdrawal, and login functionality.

---

🚀 Features

- 🔐 Login authentication for admin and users  
- 🏦 Separate accounts: Savings & Current  
- 💸 Deposit & Withdraw options  
- 📊 Mini transaction statement  
- 📩 Notifications for transactions  
- ✅ Admin and user modes supported  

---

📁 Project Structure

plaintext
elite_bank/
│
├── main.py                  # Main app entry with login and navigation
├── homepage.py              # Home screen with welcome and info
├── savings.py               # Savings account logic
├── current.py               # Current account logic
├── auth.py                  # User login system
├── models.py                # BankAccount class and transaction logic
├── notifications.py         # Notification display and mini-statement
└── requirements.txt         # List of dependencies


---

✅ Requirements

Install using pip:

bash
pip install streamlit


If using account or notification features, also add:

bash
pip install pillow


---

▶ How to Run

bash
streamlit run main.py

