#Q...write a python program to remove (i)th character
# from a string ???

s="injection"
for ch in s:
    if(ch!='i'):
        print(ch,end="")
    if(ch=='i'):
        del(ch)


