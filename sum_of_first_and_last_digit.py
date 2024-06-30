#Q..sum of first and last digit??

n=input("Enter Number:")
n=int(n)
last=n%10
while n>10:
    
    n=n//10
print("sum of first and last digit=",(n+last))

