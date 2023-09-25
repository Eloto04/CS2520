num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
num4 = int(input("Enter fourth number:"))

if ((num1 == num2 and num3 == num4)
        or (num1 == num3 and num2 == num4)
        or (num1 == num4 and num2 == num3)):
    print("two pairs")
else:
    print("not two pairs")
