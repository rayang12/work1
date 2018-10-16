def sign_up():
    sign1=input("Enter name")
    sign2=input("Enter last name")
    age=input("Enter age")
    if age>="18":
        print("You are eligible")
        sign3=input("create password")
        sign4=input("confirm password")
        if sign3==sign4:
            print("Passwords match")
        else:
            print("Passwords do not match")
    else:
        print("Not eligible")
    
sign_up()
