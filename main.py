from user import register,login,list

def mainMenu ():
 while True:
    choice=input(" Main Menu Enter:\n 1) register\n 2) Login\n 3) List Users\n 4) Exit\n")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        list()
    else:
        return
mainMenu()