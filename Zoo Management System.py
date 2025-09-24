import shelve

""" 
    Report:
            This script implements a zoo management system wth multiple functions such as:
            - creating / deleting users
            - creating / deleting animals
            - create / view / update and delete a zoo
            - searching for animals
            - creating new users (standard or admin)
            - validation on certain fields like unacceptable password format and animal tag number
            - saving and loading data to and from a file of choice using shelve module

    Sources:
    https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
    https://note.nkmk.me/en/python-dict-clear-pop-popitem-del/
"""
def displayMenu(menuType):
    """ prints out different menu layouts based on the value of menuType

    Args:
        menuType (String): the type of menu to display
    """
    
    if menuType == "main":
        print(f"{'=' * 30}\nWelcome to Zoo Management!\n{'=' * 30}")
        print("1) Manage Zoo.")
        print("2) User Accounts.")
        print("3) Exit.")
    
    elif menuType == "zoo":
        print(f"{'=' * 30}\nZoo Management Menu\n{'=' * 30}")
        print("1) Admin Zoo.")
        print("2) View Settings.")
        print("3) Update Zoo.")
        print("4) Delete Zoo.")
        print("5) Return to Main Menu.")
        
    elif menuType == "user":
        print(f"{'=' * 30}\nUser Management Menu\n{'=' * 30}")
        print("1) Add Users.")
        print("2) View Users.")
        print("3) Delete Users.")
        print("4) Return to Main Menu.")
        
    elif menuType == "adminzoo":
        print(f"{'=' * 30}\nAdmin Zoo Menu\n{'=' * 30}")
        print("1) Add Animal.")
        print("2) Query Animal.")
        print("3) Delete Animal.")
        print("4) Return to Zoo Management Menu.")
        
    elif menuType == "standardzoo":
        print(f"{'=' * 30}\nAdmin Zoo Menu\n{'=' * 30}")
        print("1) Query Animal.")
        print("2) Return to Zoo Management Menu.")

    else:
        print("ERROR. Menu could not be displayed")

def validateUser(username, password):
    """validates a username and password

    Args:
        username (string): must be only letters
        password (string): must contain both letters and numbers

    Returns:
        boolean: returns true if constraints are met, false otherwise
    """
    
    letters = False
    numbers = False
    
    # Check each character in the password
    for char in password:
        if char.isalpha():
            letters = True
        if char.isdigit():
            numbers = True
    
    if username.isalpha() and numbers and letters:
        return True
    else:
        return False
 
def manageZooCreation():
    """Function to manage zoo creation
    """
    # if no users exist
    if not users: 
        print("\nNo users exist. Please create an Admin account first.")
        username = input("Enter username (letters only): ")
        password = input("Enter password (must contain letters and numbers): ")
        
        if validateUser(username, password):
            users[username] = {"password": password, "role": "admin"}
            print("Admin profile has been successfully created! Please Log in below:\n")
        else:
            print("ERROR. Invalid username or password. Try again.\n")
            return

    # login
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # validate if entered user exists, and then if their password matches
    if username in users and users[username]["password"] == password:
        print("Login successful!\n")
        
        # check if the user is an admin
        if users[username]["role"] == "admin":
            # if zoo doesn't exist, create
            if not zoo:
                zooName = input("Enter the name of the Zoo: ")
                zoo["name"] = zooName
                print(f"\nZoo: {zooName} has been successfully created!\n")
            # if zoo did exist, display next menu
            else:
                while True:
                    displayMenu("zoo")
                    choice = input("Enter a choice: ")
                    
                    match choice:
                        # admin zoo
                        case "1":
                            while True:
                                # if user is an admin
                                if users[username]["role"] == "admin":
                                    displayMenu("adminzoo")
                                    subChoice = input("Enter a choice: ")
                                    
                                    match subChoice:
                                        # Add animal
                                        case "1":
                                            addAnimal()
                                            
                                        # Query animal
                                        case "2":
                                            queryAnimal()
                                            
                                        # Delte animal
                                        case "3":
                                            deleteAnimal()
                                            
                                        # return to zoo management    
                                        case "4":
                                            print("\nReturning to zoo management menu...\n")
                                            break
                                        
                                        # any other option
                                        case _:
                                            print("\nInvalid choice. Please try again.\n")
                                
                                # standard user
                                else:
                                    displayMenu("standardzoo")
                                    subChoice = input("\nEnter a choice: \n")
                                    
                                    match subChoice:
                                        case "1":
                                            queryAnimal()
                                            
                                        case "2":
                                            print("\nReturning to zoo management menu...\n")
                                            break
                                        
                                        case _:
                                            print("\nInvalid choice. Please try again.\n")
                                        
                                        
                        # view settings
                        case "2":
                            print(f"\nZoo Name: {zoo['name']}\n")
                        
                        # update zoo
                        case "3":
                            newZooName = input("\nEnter new Zoo name: ")
                            zoo["name"] = newZooName
                            print("Zoo name updated!")
                        
                        # delete zoo
                        case "4":
                            zoo.clear()
                            print("\nZoo deleted! returning...")
                            break
                        
                        # return to main menu
                        case "5":
                            print("\nReturning to Main Menu...\n")
                            break
                        
                        # any other option
                        case _:
                            print("\nInvalid choice.\n")
        else:
            print("ERROR. You must be an Admin to create or manage the zoo.\n")
    else:
        print("ERROR. Incorrect username or password.\n")    

def userAccounts():
    """Function to Manage user accounts.
    """    

    # if no users exists, create an admin account
    if not users:
        print("\nNo user accounts exist. Please create an Admin account first.")
        username = input("Enter username: ")
        password = input("Enter password (must contain letters and numbers): ")
        
        if validateUser(username, password):
            users[username] = {"password": password, "role": "admin"}
            print("\nAdmin account has been successfully created! Please log in below: \n")
        else:
            print("\nERROR. Invalid username or password. Try again.\n")
            return  # stop if invalid
        
    # login
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]["password"] == password:
        print("\nLogin successful!\n")
        
        # if user is an admin
        if users[username]["role"] == "admin":
            while True:
                displayMenu("user")
                choice = input("Enter a choice: ")
                
                match choice:
                    # Add User
                    case "1":
                        letters = False
                        numbers = False
                        newUsername = input("Enter new username (letters only): ")
                        newPassword = input("Enter new password (letters and numbers): ")
                        role = input("Enter user role (admin, standard): ").lower()

                        for char in newPassword:
                            if char.isalpha():
                                letters = True
                            if char.isdigit():
                                numbers = True

                        if newUsername.isalpha() and letters and numbers and role in ["admin", "standard"]:
                            if newUsername not in users:
                                users[newUsername] = {"password": newPassword, "role": role}
                                print(f"\nUser: '{newUsername}', Role: '{role}', had been successfully added\n")
                            else:
                                print("\nERROR. Username already exists!\n")
                        else:
                            print("\nERROR. Username must be letters only and password must contain both letters and numbers.\n")
                    
                    # view users
                    case "2":
                        counter = 1
                        print("\nExisting Users:")
                        for user in users.keys():
                            print(f"User {counter}) {user}")
                            counter+=1
                        print("")
                    
                    case "3":
                        # Delete User
                        deletedUser = input("Enter username to delete: ")
                        if deletedUser in users:
                            if deletedUser == username:
                                print("\nYou are this user.\n")
                            else:
                                del users[deletedUser]
                                print(f"\nUser '{deletedUser}' deleted successfully.\n")
                        else:
                            print("\nUser not found.\n")
                    
                    case "4":
                        # Return to main
                        print("\nReturning to Main Menu...\n")
                        break
                    
                    case _:
                        print("\nInvalid choice.\n")
        
        else:
            print("\nERROR. Only Admin users can manage accounts.\n")
    else:
        print("\nERROR. Invalid username or password.\n")

def addAnimal():
    """Function to add an animal to the zoo
    """
    
    name = input("Enter an animal name (letters only): ")
    tagNo = input("Enter a tag number (must contain letters and numbers): ")
    
    letters = False
    numbers = False
    
    # iterate through every charachter in tag, and updating values if it meets criteria
    for char in tagNo:
        if char.isdigit():
            numbers = True
        if char.isalpha():
            letters = True
    
    if name.isalpha() and letters and numbers:
        if tagNo not in animals:
            animals[tagNo] = name
            print(f"\nAnimal: '{name}', Tag: '{tagNo}' successfully added!\n")
        else:
            print("\nERROR. Animal already exists!\n")
    else:
        print("\nERROR. invalid name or tag\n")           
    
def deleteAnimal():
    """Function to delete an animal in the zoo
    """
    
    #loop until "finish" is entered
    while True:
        tag = input("Enter an animal tag to delete ('finish' to return): ")
        if tag.lower() == "finish":
            print("\nfinishing deletion, returning...\n")
            break
        elif tag in animals:
            del animals[tag]
            print("\nAnimal deleted successfully!\n")
        else:
            print("\nAnimal tag not found.\n")    
    
def queryAnimal():
    """Function to query animals in the zoo
    """
    # loop until "finish" is entered
    while True:
        tagNo = input("Enter a tag number to query ('finish' to return): ")
        
        if tagNo.lower() == "finish":
            print("\nFinishing search, returning...\n")
            break
    
        if tagNo in animals:
            print(f"\nAnimal found: {animals[tagNo]}\n")
        else:
            print("\nERROR. Animal does not exist in database, please try again.\n")
    
def main():
    
    while True:
        displayMenu("main")
        choice = input("Enter a choice: ")
        match choice:
            # manage zoo
            case "1":
                manageZooCreation()
            
            # user accounts
            case "2":
                userAccounts()
            
            # exit
            case "3":
                print("Saving data...")
                with shelve.open(dbName) as db:
                    db["users"] = users
                    db["zoo"] = zoo
                    db["animals"] = animals
                print("Data saved successfully. Goodbye!")
                return

            # anything else
            case _:
                print("Invalid Entry, please try again.\n")    
        
dbName = input("Enter the name of your Database: ")

# Load previous data if it exists
with shelve.open(dbName) as db:
    users = db.get("users", {})
    zoo = db.get("zoo", {})
    animals = db.get("animals", {})
main()