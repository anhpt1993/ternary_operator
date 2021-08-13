# Using ternary operator

while True:
    try:
        num = int(input("Enter a number please: "))
        break
    except Exception:
        print("Idiot! An interger, not a float or a string!")
        print()

msg = "Number {} is even".format(num) if num % 2 ==0 else "Number {} is odd".format(num)
print(msg)

