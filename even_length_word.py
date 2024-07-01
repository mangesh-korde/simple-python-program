#Q...Write a python program to print Even length words in a string???


s="shrirampur rbnb cdj college sham"
s1=s.split()
for val in s1:
    if len(val)%2==0:
        print(val)
#print(s1)
