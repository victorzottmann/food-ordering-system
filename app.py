import os

restaurants = [
    {
        "name": "The Tavern", 
        "category": "Japanese", 
        "active": False
    },
    {
        "name": "Supreme Pizza",
        "category": "Italian",
        "active": True
    },
    {
        "name": "The Canteen",
        "category": "Mediterranean",
        "active": True
    }
]

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
                list_restaurants()
                break
            case 3:
                # activate_restaurant()
                break
            case 4:
                exit_program()
                break

def register_restaurant():
    show_option_title("Register a new restaurant\n")
    name = input("Enter a name for the restaurant: ")
    restaurants.append(name)
    print(f"Restaurant successfully registered!\n")
    return_to_menu()
  
def list_restaurants():
    show_option_title("All restaurants registered:\n")
    for restaurant in restaurants:
        name = restaurant["name"]
        category = restaurant["category"]
        active = restaurant["active"]
        print(f"- {name} | {category} | {active}", sep="\n") 
    return_to_menu()       

def show_option_title(title):
    os.system("clear")
    print(title)

def return_to_menu():
    input("\nPress any key to return to the main menu: ")
    main()   

def main():
    display_menu()
    select_option()
  
if __name__ == "__main__":
    main()