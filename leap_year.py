year = int (input("Enter the year to check: "))
if (year>0):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("It is a leap year ")
    else:
        print("No it is a leap year ")
else:
    print("Enter a valid option")
