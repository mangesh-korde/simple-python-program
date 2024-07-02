#Q..write python program to remove all duplicates
#  from a given string???

s=input("Enter String:")
s1=""  #empty string
for ch in s:
    if ch not in s1:
        s1=s1+ch  #concated
print("After delete duplicates:")
print(s1)
        
