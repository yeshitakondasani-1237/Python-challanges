mixed_list = []
number_list = []
string_list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    values = input("Enter value: ")
    if values.isdigit():
        mixed_list.append(int(values))
    elif "." in values and values.replace(".", "").isdigit():
        mixed_list.append(float(values))
    else:
        mixed_list.append(values)
for value in mixed_list:
    if type(value) == int:
        number_list.append(value)
    elif type(value) == float:
        number_list.append(value)
    elif type(value) == str and value != "":
        string_list.append(value)
    else:
        print("Invalid input")
section = input("Enter section: ")
if section == "A":
    print("Number List:", number_list)
    print("Total Numbers:", len(number_list))
elif section == "B":
    print("String List:", string_list)
    print("Total Strings:", len(string_list))
elif section == "C":
    print("Number List:", number_list)
    print("String List:", string_list)
    print("Total Numbers:", len(number_list))
    print("Total Strings:", len(string_list))
else:
    print("Invalid Section")