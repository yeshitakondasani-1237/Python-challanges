name = input("Enter your name: ")
n = int(input("Enter the number of students: "))

valid_list = []
failed_list = []

has_vowel = any(v in name.lower() for v in "aeiou")

for i in range(n):
    mark = int(input("Enter marks: "))

    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")

    elif mark >= 90:
        print(mark, "→ Excellent work" if has_vowel else "→ Excellent")
        valid_list.append(mark)

    elif mark >= 75:
        print(mark, "→ Very Good+" if has_vowel else "→ Very Good")
        valid_list.append(mark)

    elif mark >= 60:
        print(mark, "→ Good+" if has_vowel else "→ Good")
        valid_list.append(mark)

    elif mark >= 40:
        print(mark, "→ Average+" if has_vowel else "→ Average")
        valid_list.append(mark)

    else:
        print(mark, "→ Its ok, try again next time" if has_vowel else "→ Fail")
        failed_list.append(mark)

print("\nFinal Summary:")
print("Total Valid Students:", len(valid_list))
print("Total Failed Students:", len(failed_list))
