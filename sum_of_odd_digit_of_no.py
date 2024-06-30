#Q..print sum of ODD digits from a Number??
n=input("Enter number:")
n=int(n)
sum=0
while n>0:
     if(n%2!=0):
         sum=sum+(n%10)
     n=n//10

print("sum of odd digit=",sum)
