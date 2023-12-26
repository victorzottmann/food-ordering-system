import os

restaurants = []

def display_menu():
    # os.system("cls") # on windows
    os.system("clear") # on mac / linux
    
    print("""
    ▀█▀ ▄▀█ █▀ ▀█▀ █▄█   ▀█▀ ▄▀█ █▄▄ █░░ █▀▀
    ░█░ █▀█ ▄█ ░█░ ░█░   ░█░ █▀█ █▄█ █▄▄ ██▄
    """)
    
    print("1. Register restaurant")
    print("2. List restaurant")
    print("3. Activate restaurant")
    print("4. Exit\n")
  
def exit_program():
    print("Bye!")
  
def select_option():
    while True:
        option = int(input("Choose an option between 1 to 4: "))
        match option:
            case 1:
                register_restaurant()
                break
            case 2:
                # list_restaurant()
                break
            case 3:
                # activate_restaurant()
                break
            case 4:
                exit_program()
                break

def register_restaurant():
    os.system("clear")
    print("Register a new restaurant\n")
    name = input("Enter a name for the restaurant: ")
    restaurants.append(name)
    print(f"Restaurant successfully registered!\n")
    input("Press any key to return to the main menu")
    main()
  
def list_restaurant():
    pass

def main():
    display_menu()
    select_option()
  
if __name__ == "__main__":
    main()