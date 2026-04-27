########## Main application entry point ############
class App:
    def __init__(self):
        # Initialize the application
        # Create lists to hold active and disabled users
        self.active_user_lst = []
        self.disabled_user_lst = []

        # Initialize the menu with options
        self.menu = Menu("Main Menu", {"1": "Add User", 
                                       "2": "View active and disabled users", 
                                       "3": """Enable/Disable Users""",
                                       "4": "Test login",
                                      "0": "Exit"
        })

    def run(self):
        while True:
            self.menu.display()
            choice = self.menu.get_choice()
            if choice == "0":
                print("Exiting application.")
                break
            elif choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
          

# Placeholder Menu class
class Menu:

    # Initialize the menu with a title and options
    def __init__(self, title, options):
        self.title = title
        self.options = options

    # Displays Menu
    def display(self):
        # Displays menu name
        print(f"\n{self.title}")
        # Displays menu options by iterating through the options dictionary
        for key in self.options.keys():
            print(f"{key} - {self.options[key]}")
    
    # Gets user input for menu choice and validates it
    def get_choice(self):
        while True:

            # Get user input for menu choice
            choice = input("Enter your choice: ")

            # Validate user input against available options
            if choice in self.options:
                return choice
            else:
                print("Invalid choice. Please try again.")
                self.display
            

# Placeholder User class
class User:
    def __init__(self, name):
        self.name = name
        print(f"User {self.name} initialized")

    def login(self):
        print(f"User {self.name} logged in")

########## Main application ##########
if __name__ == "__main__":
    app = App()
    app.run()