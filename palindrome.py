#check no is palindrome or not??

n=input("Enter Number:")
n=int(n)
n1=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10

if(rev==n1):
    print("Number is palindrome...")
else:
    print("Number is not Palindrome..")
