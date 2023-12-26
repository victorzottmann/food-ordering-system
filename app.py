import sys

print("""
▀█▀ ▄▀█ █▀ ▀█▀ █▄█   ▀█▀ ▄▀█ █▄▄ █░░ █▀▀
░█░ █▀█ ▄█ ░█░ ░█░   ░█░ █▀█ █▄█ █▄▄ ██▄
""")

print("1. Register restaurant")
print("2. List restaurant")
print("3. Activate restaurant")
print("4. Exit\n")

while True:
  option = int(input("Choose an option between 1 to 4: "))
  
  if option == 1:
    print("Register restaurant")
    break
  if option == 2:
    print("List restaurant")
    break
  if option == 3:
    print("Activate restaurant")
    break
  if option == 4:
    print("Exit")
    break