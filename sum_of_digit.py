#Q..sum of digit??

n=input("Enter Number:")
n=int(n)
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("sum of digit=",sum)
