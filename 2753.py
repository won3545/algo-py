# 2753
# input
year = input()
year = int(year)
# output
if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("1")
        else:
            print("0")
    else:
        print("1")
else:
    print("0")