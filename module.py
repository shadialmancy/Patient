loginList=[["admin","admin"]]
patientList=[["none","none","none","none","none"]]
def Register(email,passw):
    if email.find("@")==-1:
        print("Error: This email is unvalid.")
        return True
    elif isDuplicated(email):
        print("Error: this email is already been used.")
        return True
    else:
        loginList.append([email,passw])
        print("Registeration Complete!")
        return False

def isDuplicated(email):
    for i in range(len(loginList)):
            for j in range (len(loginList[i])):
                if email ==loginList[i][0]:
                    return True
    return False

def Login(email,password):
    for i in range(len(loginList)):
            for j in range (len(loginList[i])):
                if email == loginList[i][0] and password == loginList[i][1]:
                    return False
    print("Incorrect Email or password")
    return True

def addPatient(id,name,phone,bloodType,date):
    for i in range(len(patientList)):
        if id == patientList[i][0]:
            print("Error id already used")
            return True
    patientList.append([id,name,phone,bloodType,date])
    print("Added Successfully")
    return False

def deletePatient(id):
    for i in range(len(patientList)):
        if id == patientList[i][0]:
            patientList.pop(i)
            print("Deleted Successfully")
            return False
            
    print("Error: this id is not available")
    return True

def editPatient(id,name,phone,bloodType,date):
    for i in range(len(patientList)):
        if id == patientList[i][0]:
            patientList.pop(i)
            patientList.append([id,name,phone,bloodType,date])
            print("Edited Successfully")
            return False
            
    print("Error: this id is not available")
    return True

def searchPatient(id):
     for i in range(len(patientList)):
                if id == patientList[i][0]:
                    print(patientList[i])
                    return False
     print("Error: this id is not available")
     return True

def showAll():
    count=0
    for i in patientList:
        print(i)
    choice=input("Fliter:\n\
        1-date\n\
        2-Blood Type\n")
    choice = choice.lower()
    if choice == '1' or choice == "date":
        date=input("Enter the date: ")
        for i in range(len(patientList)):
            if date == patientList[i][-1]:
                print(patientList[i])
                count+=1
        if count == 0:
            print("not found")
    elif choice == '2' or choice == "blood":
        bloodType=input("Enter the Blood Type: ")
        for i in range(len(patientList)):
            if bloodType == patientList[i][-2]:
                print(patientList[i])
                count+=1
        if count == 0:
            print("not found")
    else:
        print("not found")







                    


            