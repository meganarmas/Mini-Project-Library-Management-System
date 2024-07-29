from Modules.class_users import UserClass

users = []


def user_op_menu(self):
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Enter choice: ")

    if choice == '1':
        self.add_new_user()
    elif choice == '2':
        self.view_users()
    elif choice == '3':
        self.display_all_details()
    else:
        print("Please enter a valid number.")
    

def add_new_user(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        library_id = input("Enter library ID: ")
        new_user = {'First Name': first_name, 'Last Name': last_name, 'Library Id': library_id}
        users.append(new_user)
        print(f"{new_user} has been added.")

def view_users(self):
        library_id = input("Enter library ID of user: ")
        for user in users:
            if UserClass.get_library_id() == library_id:                
                print(f"{user}found!")
                print(f"First Name: {UserClass.get_first_name}, Last Name: {UserClass.get_last_name}, Library ID: {UserClass.get_library_id}")
        else:
            print("User was not found.")

def display_all_details(self):
    for user in users:
        print(f"First name: {user["First name"]} Last name: {user["Last name"]}")
        print(f"Library ID: {user["Library Id"]}")