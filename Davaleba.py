word = input("შეიყვანე სიტყვა: ")
symbol = input("რომელი სიმბოლო დავთვალოთ: ")

count = 0

for char in word:
    if char == symbol:
        count += 1

print("სიმბოლო", symbol, "გვხვდება", count, "-ჯერ")
