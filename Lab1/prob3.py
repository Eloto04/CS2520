month = input("Enter a month: ")
day = int(input("Enter a day: "))

monthsWith30 = ["April", "June", "September", "November"]

if ((month == "February" and day > 28)
        or (month in monthsWith30 and day > 30)
        or (day > 31)
        or (day <= 0)):
    print("Invalid")
elif ((month == "March" and day >= 20)
        or (month == "April" or month == "May")
        or (month == "June" and day <= 20)):
    print("Spring")
elif ((month == "June" and day >= 21)
        or (month == "July" or month == "August")
        or (month == "September" and day <= 21)):
    print("Summer")
elif ((month == "September" and day >= 22)
        or (month == "October" or month == "November")
        or (month == "December" and day <= 20)):
    print("Autumn")
elif ((month == "December" and day >= 21)
        or (month == "January" or month == "February")
        or (month == "March" and day <= 19)):
    print("Winter")