#Q..check no is Armstrong or not??

n=input("Enter no:")
n=int(n)
n1=n
arm=0
while n>0:
    d=n%10
    arm=arm+(d*d*d)
    n=n//10
if(n1==arm):
    print("Number is Armstromg...")
else:
    print("NUmber is not Armstrong...")
