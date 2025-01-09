num = int(input("Enter The Number"))

if num < 0:
    print("Enter A positve Number")
else:
    digits = 0
    while num > 0:
        num //= 10
        digits += 1
print("The Number Of Digits In The Number:", digits)
