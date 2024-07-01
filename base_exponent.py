#Q..Write a program to calculate X raise to y??


x=input("Enter the base:")
x=int(x)
y=input("Enter the Exponent:")
y=int(y)
ans=1
for i in range(1,y+1):
    ans=ans*x

print("ans=",ans)
