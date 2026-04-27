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
        # laceholder for the main application logic
        print("App is running")

# Placeholder Menu class
class Menu:

    # Initialize the menu with a title and options
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        # Displays menu name
        print(f"\n{self.title}")
        # Displays menu options by iterating through the options dictionary
        for key in self.options.keys():
            print(f"{key} - {self.options[key]}")

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