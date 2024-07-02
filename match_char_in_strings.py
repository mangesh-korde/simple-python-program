#Q..count no of matching characters in two strings???
s="karan"
s1="sitaram"
cnt=0
for ch in s:
    if ch in s1:
        cnt=cnt+1
print("counted character=",cnt)
 
