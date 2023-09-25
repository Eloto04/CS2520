time1 = int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))

timeDiff = max(time1, time2) - min(time1, time2)
hours = timeDiff // 100
minutes = timeDiff % 100

print(f'{hours} hours {minutes} minutes')