import os

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
        # register_restaurant()
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
  
def main():
  display_menu()
  select_option()
  
if __name__ == "__main__":
  main()