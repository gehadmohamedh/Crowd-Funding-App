import time 
import re 
from helpers import readNum,readString,validateEmail
from project import mainProject

def register ():
    id = round(time.time())
    fname = readString("Enter Your First Name ")
    lname = readString("Enter Your last Name ")
    email = validateEmail()
    password = input("Enter Your Password")
    phone = readNum("Enter Your Phone Number")
    user_info = f"{id}:{fname}:{lname}:{email}:{password}:{phone}\n"
    
    try :
        file = open("users_data.txt",'a')
        file.write(user_info)
    except Exception as e:
        print(e)

    
def list():
    try :
        file = open("users_data.txt",'r')
        users = file.readlines()
        for user in users :
            print(user.strip("\n"))
    except Exception as e:
        print(e)

def login ():
    email = input("Enter Your Email")
    password = input("Enter Your Password")

    try :
        file = open("users_data.txt",'r')
        users = file.readlines()

    except Exception as e:
        print(e)

    else:
        found = False
        for index , user in enumerate(users):
            cur_user = user.strip("\n").split(":")[3:5]
            if email==cur_user[0] and str(password) == str(cur_user[1]):
                cur_info = user.strip("\n").split(":")[0:3]
                print("Welcome "+cur_info[1]+" "+cur_info[2])
                mainProject(cur_info[0])
                found=True
                return user 
        if not found:
            print("The email or Password Is Incorrect")    

                
