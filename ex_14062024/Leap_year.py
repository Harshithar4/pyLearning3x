year = int(input("Enter the year you want to check: \n"))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is Leap year")
    elif year % 400 == 0:
        print(f"{year} is Leap year")
else:
    print(f"{year} is Not Leap year")
