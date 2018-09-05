mydict={"Shivani":'Abcd@11',"Saloni":'Efgh@12'}

def upassword(password):
    validu=0
    validd=0
    validsc=0
    for i in password:
        if i.isupper():
            validu=validu+1
        elif i in '1234567890':
            validd=validd+1
        elif i in '!@#$%^&*':
            validsc=validsc+1
    if(validu>0 and validd>0 and validsc>0 and len(password)>=6 and len(password)<=20):
        return True
    else:
        return False

insert='y'
while(insert=='y' or insert=='Y'):    
    username=input("Enter the user name")
    if username in mydict:
        VorM=input("Do you want to view or modify?")
        if(VorM=='view'):
            print("Your username is:",username)
            print("Your password is:",mydict[username])

        elif(VorM=='modify'):
        
    
            chance=3
            while(chance>0):
                password1=input("Password:")
                if(upassword(password1)):
                    mydict[username]=password1
                    print(mydict[username])
                    break
                else:
                    chance=chance-1
                    print("invalid")
                
            if(chance<=0):
                print("Updation failed")
    else:
        if((" " not in username) and (username[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") and  len(username)>=6 and len(username)<=12):
        
            chance=3
            while(chance>0):
                password1=input("Enter password")
                if(upassword(password1)):
                    mydict[username]=password1
                    break
                else:
                    chance=chance-1
                    print("Invalid")
            if(chance<=0):
                print("Updation failed")

        else:
            print("Please enter a proper username")
        
    print(mydict)
    insert=input("Want to insert?Y/N")
                
        
