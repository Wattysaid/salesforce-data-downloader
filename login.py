# login.py

from simple_salesforce import Salesforce
import getpass

def login_to_salesforce():
    print("Please enter your Salesforce login details:")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    security_token = getpass.getpass("Security Token: ")

    try:
        sf = Salesforce(username=username, password=password, security_token=security_token)
        print("Login successful!")
        return sf
    except Exception as e:
        print(f"Login failed: {e}")
        return None

if __name__ == "__main__":
    sf = login_to_salesforce()
