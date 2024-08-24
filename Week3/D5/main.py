def main_menu():
    print("Welcome to the Health Tracker!")
    logged_in_user = None # Track the logged-in user

    while True:
     if not logged_in_user:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        
