import os
import csv

########## Main application entry point ############
class App:
    """
    The main controller class that handles data loading, 
    user management, and the primary application loop.
    """
    def __init__(self):
        # Initialize storage for user objects categorized by status
        self.active_user_lst = []
        self.disabled_user_lst = []
        self.all_user_lst = []
        self.menu = None
        self.filename = 'users.csv'

    def save_data(self):
            """
            Overwrites the users.csv file with the current state of all_user_lst.
            """
            try:
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    # Write the header first
                    writer.writerow(['username', 'status', 'password'])
                    
                    # Write each user from the master list
                    for user in self.all_user_lst:
                        writer.writerow([user.name, user.status, user.password])
                print("Data saved successfully.")
            except Exception as e:
                print(f"An error occurred while saving: {e}")

    def load_data(self):
        """
        Ensures the data file exists, populates the master user list,
        and triggers the sorting of users and menu initialization.
        """
        # Check if the file already exists
        if os.path.exists(self.filename):
            print(f"'{self.filename}' found. Opening the file...")
            
            # Open and read the existing CSV file
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                # Skip header if it exists (Optional improvement: next(reader))
                for user in reader:
                    # Create User objects from CSV rows (Index 0: name, 2: password, 1: status)
                    self.all_user_lst.append(User(user[0], user[2], user[1]))
                    
        else:
            print(f"'{self.filename}' not found. Creating a new one...")
            
            # Create a new CSV file by opening it in write mode ('w')
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write a header row to define data structure
                writer.writerow(['username', 'status', 'password'])

        # Populate the specific active/disabled lists and set up the UI
        self.load_users()
        self.load_menu()

    def load_users(self):
        """
        Reads the CSV file and sorts users into active or disabled lists based on status.
        """
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for user in reader:
                # user[1] corresponds to the 'status' column
                if user[1] == "active":
                    self.active_user_lst.append(User(user[0], user[2], user[1]))
                elif user[1] == "disabled":
                    self.disabled_user_lst.append(User(user[0], user[2], user[1]))

    def load_menu(self):
        """Initializes the Menu object with navigation options."""
        self.menu = Menu("Main Menu", {
            "1": "Add User", 
            "2": "View active and disabled users", 
            "3": "Enable/Disable Users",
            "4": "Test login",
            "0": "Exit"
        })

    def run(self):
        """The main application engine that processes user input in a loop."""
        self.load_data()
        while True:
            self.menu.display()
            choice = self.menu.get_choice()

            if choice == "0":
                self.save_data()  # Ensure data is saved before exiting 
                print("Exiting application.")
                break

            elif choice == "1":
                # Calls the static-like add_user method and updates local list
                new_user = User.add_user(self)
                self.active_user_lst.append(new_user)
                print(f"User {new_user.name} added successfully.")

            elif choice == "2":
                # Display categorized users
                print("\nActive Users:")
                for user in self.active_user_lst:
                    print(user)
                print("\nDisabled Users:")
                for user in self.disabled_user_lst:
                    print(user)

            elif choice == "3":
                # Logic for toggling user status
                print("Type the username of the user you want to enable/disable:")
                username = input().strip()
               
                for user in self.all_user_lst:
                    if user.name == username:
                        if user.status == "active":
                            user.disable()
                            self.active_user_lst.remove(user)
                            self.disabled_user_lst.append(user)
                            print(f"User {user.name} has been disabled.")
                        elif user.status == "disabled":
                            user.enable()
                            self.disabled_user_lst.remove(user)
                            self.active_user_lst.append(user)
                            print(f"User {user.name} has been enabled.")

                        elif choice == "4":
                            # Example: Picking the first user in the list to test
                            if self.active_user_lst:
                                test_user = self.active_user_lst[0]
                                test_user.login()
                            else:
                                print("No active users available to test.")

class Menu:
    """Handles the terminal-based user interface."""
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        """Prints the menu title and formatted options."""
        print(f"\n{self.title}")
        for key in self.options.keys():
            print(f"{key} - {self.options[key]}")
    
    def get_choice(self):
        """Prompts user for input and ensures the choice exists in options."""
        while True:
            choice = input("Enter your choice: ")
            if choice in self.options:
                return choice
            else:
                print("Invalid choice. Please try again.")
                self.display()
            

class User:
    """Represents an individual user entity and handles user-specific actions."""
    def __init__(self, name, password = '', status = "active"):
        self.name = name
        self.password = password
        self.status = status
        
    def login(self):
            """
            Attempts to authenticate the user. 
            Provides an option to cancel and return to the main menu.
            """
            while True:
                print("\n--- Login (Type 'cancel' to return) ---")
                username = input("Enter username: ").strip()
                
                # Check for cancel at the first prompt
                if username.lower() == 'cancel':
                    print("Login cancelled.")
                    return False # Returning False tells the App the login didn't happen

                password = input("Enter password: ").strip()
                
                # Check for cancel at the second prompt
                if password.lower() == 'cancel':
                    print("Login cancelled.")
                    return False

                # Validate credentials
                if username == self.name and password == self.password:
                    print(f"Login successful. Welcome, {self.name}!")
                    return True # Returning True confirms a successful login
                else:
                    print("Login failed. Incorrect username or password.")
                    print("Please try again or type 'cancel'.")
                    

    def add_user(self):
        """
        Prompts for a new username and ensures it is unique 
        before saving to the CSV and returning a new User object.
        """
        while True:
            user_name = input("Enter username (or type 'cancel'): ").strip()
            
            if user_name.lower() == 'cancel':
                return None # Signal that the operation was aborted

            # Check if the name already exists in the master list
            # Note: 'self' here refers to the App instance passed in from choice == "1"
            username_exists = any(user.name == user_name for user in self.all_user_lst)

            if username_exists:
                print(f"Error: The username '{user_name}' is already taken. Please try another.")
            elif not user_name:
                print("Error: Username cannot be empty.")
            else:
                # If unique, break the loop and continue to password setup
                break

        print("Would you like to set a password? (y/n)")
        set_password = input().lower()
        if set_password == "y":
            try:
                password = input("Enter password: ").strip()
            except AttributeError as e:
                print(f"Error setting password: {e}")
                password = ''
        else:
            password = ''

        # Persistence: Append to CSV
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_name, "active", password])

        # Return the new User object
        new_created_user = User(user_name, password)

        # Also add it to the master list so it's tracked for future duplicate checks
        self.all_user_lst.append(new_created_user)

        return new_created_user

    def disable(self):
        """Updates status to disabled."""
        self.status = "disabled"

    def enable(self):
        """Updates status to active."""
        self.status = "active"

    def __str__(self):
        """String representation for easy printing."""
        return f"User: {self.name}, Status: {self.status}"

########## Main application execution ##########
if __name__ == "__main__":
    app = App()
    app.run()