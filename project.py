import time 
from helpers import readNum,readString,validateDate


def mainProject (user_id ):
    while True:
        choice=input(" Projects Menu Enter:\n 1) New project\n 2) List projects\n 3) Edit projects\n 4) Delete projects\n 5) Exit\n")
        if choice == '1':
            create(user_id)
        elif choice == '2':
            list(user_id)
        elif choice == '3':
            edit(user_id)
        elif choice == '4':
            delete(user_id)
        else:
            return
        

def create(user_id):
    id = round(time.time())
    title = readString("Enter Title ")
    details = input("Enter Description Of the Project ")
    target = readNum("Enter Target ")
    start = validateDate("Enter Start Date YYYY-MM-DD ")
    end = validateDate("Enter End Date YYYY-MM-DD ")

    project_info = f"{user_id}:{title}:{details}:{target}:{start}:{end}\n"
    try :
        file = open("project_data.txt",'a')
        file.write(project_info)
    except Exception as e:
        print(e)



def list (user_id):

    try :
        file = open("project_data.txt","r")
        projects = file.readlines()

    except Exception as e:
        print(e)

    else:
        found = False
        counter=0

        for index , project  in enumerate(projects):
            proj_uder_id = project.strip("\n").split(":")[0]

            if proj_uder_id == str(user_id):
               counter+=1
               found=True
               print (str(counter)+")"+project.strip('\n')+"\n")

        if not found:
            print("There is No Projects")   



def delete (user_id):
    title = readString("Enter Title")

    try :
        file = open("project_data.txt","r+")
        projects = file.readlines()

    except Exception as e:
        print(e)
    else:
        found = False
        for index , project  in enumerate(projects):
            cur_info = project.strip("\n").split(":")[0:2]

            if title == cur_info[1] and cur_info[0]== str(user_id):
               projects.pop(index)
               file.seek(0)
               file.truncate()
               found=True
               file.write( ''.join(projects))
               break

        if not found:
            print("There is No Projects With this Title")   

def edit (user_id):
    title = readString("Enter Title")
    choice=input("Enter witch feild You Wnat to Edit \n 1) title \n 2) details \n 3) target \n 4) start date \n 5) end date \n 6) Exit\n")

    if choice=='6':
       return
    if choice=='1':
       value = readString("Enter Title ")
    elif choice=='2':
      value = input("Enter Description Of the Project ")
    elif choice=='3':    
       value = readNum("Enter Target ")
    elif choice=='4':
       value = validateDate("Enter Start Date YYYY-MM-DD ")
    elif choice=='5':
        value = validateDate("Enter End Date YYYY-MM-DD ")

    try :
        file = open("project_data.txt","r+")
        projects = file.readlines()

    except Exception as e:
        print(e)
    else:
        found = False
        for index , project  in enumerate(projects):
            cur_info = project.strip("\n").split(":")[0:2]

            if title == cur_info[1] and cur_info[0]== str(user_id):
               proj = project.strip("\n").split(":")
               proj[int(choice)]=str(value)
               projects[index]= ':'.join(proj)
               projects[index]+='\n'
               print( projects[index])
               file.seek(0)
               file.truncate()
               found=True
               file.write( ''.join(projects))
               break

        if not found:
            print("There is No Projects With this Title")   
#mainProject(1680613709)