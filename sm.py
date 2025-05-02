import calendar
y = int(input("Enter a number: "))
cal  = int(input("Enter month number: "))

def print_cal( y,):
    for i in range(1,13):
        print(calendar.month(y, i)) 

print_cal(y)