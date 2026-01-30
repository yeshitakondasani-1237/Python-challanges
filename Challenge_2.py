Student_id=input("Enter Student ID : ")
Email_id= input("Enter Email ID : ")
Password= input("Enter Password : ")
Ref_code= input("Enter Ref Code : ")

first = Email_id[0]

if len(Student_id)==7:
    if Student_id[0:4] == "CSE-":
        if "0" <= Student_id[4] <= "9" and "0" <= Student_id[5] <= "9" and "0" <= Student_id[6] <= "9":
            if first != "@" and first != "." and Email_id.count("@") == 1 and Email_id.count(
                    ".") >= 1 and Email_id.count(" ") == 0:
                if Email_id[-4:] == ".edu":
                    if len(Password) >= 8 and "A" <= Password[0]<= "Z":
                        if "0" <= Password[0] <= "9" or "0" <= Password[1] <= "9" or "0" <= Password[2] <= "9" or "0" <= Password[3] <= "9" or "0" <= Password[4] <= "9" or "0" <= Password[5] <= "9" or "0" <= Password[6] <= "9" or "0" <= Password[7] <= "9":
                            if Ref_code[0:3]=="REF" and "0"<=Ref_code[3]<="9" and "0"<=Ref_code[4]<="9" and Ref_code[5]=="@":
                                print("APPROVED")
                            else:
                                print("REJECTED")
                        else:
                            print("REJECTED")
                    else:
                        print("REJECTED")
                else:
                    print("REJECTED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")
