#Q...Accept a string and count consonants in that string??

s="shrirampur"
v="aeiouAIEOU"
cnt=0
for ch in s:
    if ch not in v:
        cnt=cnt+1
print("Counted conso=",cnt)
