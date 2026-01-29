Full_Name = input("Enter Full Name : ")
Email_ID = input("Enter Email ID : ")
Mobile_number = input("Enter Mobile Number : ")
Age = int(input("Enter Age : "))

first = Email_ID[0]

if Full_Name[0] != " " and Full_Name[len(Full_Name)-1] != " " and Full_Name.count(" ") >= 1:

    if first != "@" and first != "." and (('a' <= first <= 'z') or ('A' <= first <= 'Z') or ('0' <= first <= '9')) \
       and Email_ID.count("@") == 1 and Email_ID.count(".") >= 1 and Email_ID.count(" ") == 0:

        if len(Mobile_number) == 10 and Mobile_number[0] != '0' and Mobile_number.isdigit():

            if Age >= 18 and Age <= 60:
                print("User Profile is VALID")
            else:
                print("User Profile is NOT VALID")

        else:
            print("User Profile is NOT VALID")

    else:
        print("User Profile is NOT VALID")

else:
    print("User Profile is NOT VALID")
