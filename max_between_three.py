#Q...write a python program to find the
#    MAX of three nos???

a=int(input("Enter First no:"))
b=int(input("Enter Second no:"))
c=int(input("Enter Third no:"))
if a>b and a>c:
    print("greater no=",a)
elif b>a and b>c:
    print("greater no=",b)
else:
    print("greater no=",c)
