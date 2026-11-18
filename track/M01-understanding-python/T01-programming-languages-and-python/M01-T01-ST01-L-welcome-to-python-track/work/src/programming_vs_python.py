percentage = int(input("enter the  percentage :"))
active_backlog=int(input("enter the backlog history :"))

if percentage>=60 and active_backlog==0:
    print("eligible")
else:
    print("not eligible")

