password = "python2024"

for attempt in range(3):
    user_password = input("შეიყვანე პაროლი: ")

    if user_password == "":
        continue

    if user_password == password:
        print("წვდომა დაშვებულია")
        break

    remaining = 2 - attempt
    print("არასწორი პაროლი. დარჩენილი მცდელობა:", remaining)

else:
    print("ანგარიში დაბლოკილია")


