string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")

if string1 < string2 and string1 < string3:
    print(string1)
    print(string2 if string2 < string3 else string3)
    print(string3 if string2 < string3 else string2)
elif string2 < string1 and string2 < string3:
    print(string2)
    print(string1 if string1 < string3 else string3)
    print(string3 if string1 < string3 else string1)
elif string3 < string1 and string3 < string2:
    print(string3)
    print(string1 if string1 < string2 else string2)
    print(string2 if string1 < string2 else string1)