import os


#functions
def mainMenu():
    print(":::Main menu:::")
    print("[1].Register a new user")
    print("[2].List all users")
    print("[3].Search user")
    print("[4].Delete user")
    print("[5].Update user")
    print("[6].Show active users")
    print("[7].Show inactive user")
    print("[8].Exit")

#Main
while True:
    os.system("clear")    
    mainMenu()
    opt = input("Press any option [1-8]: ")
    match opt:
        case "1":
            os.system("clear")
            print(":::Register form:::")
            id=input("Ident.number: ")
            firstname= input("Firstname: ")
            lastname= input("Lastname: ")
            mobile.phone =input("Mobile phone: ")
            email= input("E-mail: ")
            gender= input("Gender [M/F/O]: ")
            ids.append(id)
            firstnames.append(firstname)
            lastnames.append(lastname)
            mobile.phones.append(mobile.phone)
            statuses.append(True)

            createLat.append(date.today())
            print("user has been created successfully!!")

            any_key=input("Press any key to back to Main Menu")

        case "2":
            print("List all register user:::")
            print()


            any_key=input("Press any key")
        case "8":
            any_key=input("Bye,Bye. Press any Key...")
            break

        case _:
            any_key=input("Invalid option. Press any key to try again")
            print("")
            
            
            
