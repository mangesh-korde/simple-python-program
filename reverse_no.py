#convert no into Reverse No??

n=input("Enter Number:")
n=int(n)
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10

print("Reverse No=",rev)
