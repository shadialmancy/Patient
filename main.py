import module as mod
from datetime import date

print("--------------Welcome to patient's data--------------")

while True:
    done=True
    
    while True:
        done=True
        choice1=input("What do you like to choose:\n\
        1-Login\n\
        2-Register\n")
        choice1=choice1.lower()
        if choice1 == '1' or choice1 == 'login':
            while done:
                em=input("Email:")
                passw=input("Password:")
                done = mod.Login(em,passw)
            else:
                while True:
                    done=True
                    choice2=input("Choose option:\n\
                    1-Add patient\n\
                    2-Delete patient\n\
                    3-Edit patient\n\
                    4-Search patient\n\
                    5-Show All\n\
                    6-Logout\n")
                    choice2 = choice2.lower()
                    if choice2 == '1' or choice2 == 'add':
                        while done:
                            try:
                                id = int(input ("ID:"))
                                name = input ("name:")
                                phone = int(input ("phone:"))
                                bloodType = input ("bloodType:")
                                today = str(date.today())
                                print(today)
                                done=mod.addPatient(id,name,phone,bloodType,today)
                            except ValueError:
                                print("Numeric only")
                    elif choice2 == '2' or choice2 == 'delete':
                        while done:
                            try:
                                id = int(input ("ID:"))
                                done=mod.deletePatient(id)
                            except ValueError:
                                print("Numeric only")
                    elif choice2 == '3' or choice2 == 'edit':
                        while done:
                            try:
                                print("Enter the ID: ")
                                id = int(input ("ID:"))
                                if mod.searchPatient(id) == True:
                                    continue
                                name = input ("name:")
                                phone = int(input ("phone:"))
                                bloodType = input ("bloodType:")
                                today = date.today()
                                done = mod.editPatient(id,name,phone,bloodType,str(today))
                            except ValueError:
                                print("Numeric only")
                    elif choice2 == '4' or choice2 == 'search':
                        while done:
                            try:
                                id = int(input ("ID:"))
                                done = mod.searchPatient(id)
                            except ValueError:
                                print("Numeric only")
                    elif choice2 == '5' or choice2 == 'show':
                        mod.showAll()
                    elif choice2 == '6' or choice2 == 'logout':
                        break
        elif choice1 == '2' or choice1 == 'register':
            while done:
                email=input("Email: ")
                password=input("password: ")
                done = mod.Register(email,password)
        else:
            print("invalid option")



    