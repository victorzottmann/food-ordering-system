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
        "active": False
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
    print("2. List all restaurants")
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
                toggle_active_restaurant()
                break
            case 4:
                exit_program()
                break

def register_restaurant():
    show_option_title("Register a new restaurant\n")
    name = input("Enter a name for the restaurant: ")
    category = input("Enter the category of the restaurant: ")
    data = {
        "name": name,
        "category": category,
        "active": False
    }
    restaurants.append(data)
    print(f"Restaurant successfully registered!\n")
    return_to_menu()
  
def list_restaurants():
    show_option_title("All restaurants registered:\n")
    for restaurant in restaurants:
        name = restaurant["name"]
        category = restaurant["category"]
        active = "activated" if restaurant["active"] else "deactivated"
        print(f"- {name} | {category} | {active}", sep="\n") 
    return_to_menu()       

def toggle_active_restaurant():
    show_option_title("Activate / Deactivate Restaurant\n")
    name_restaurant = input("Enter the name of the restaurant: ")
    found = False
    for restaurant in restaurants:
        if name_restaurant == restaurant["name"]:
            found = True
            restaurant["active"] = not restaurant["active"]
            if restaurant["active"] == True:
                message = f"Activated"
            else:
                message = f"Deactivated"
            print(message)
            return_to_menu()
    if not found:
        print("Restaurant not found")
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