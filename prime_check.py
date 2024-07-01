# Q..Check no is prime or not??

n=input("Enter Number:")
n=int(n)
for i in range(2,n+1):
    if n%i==0:
        break
if(i==n):
    print("Number is prime...")
else:
    print("Number not prime...")
