#Q...Accept a string and count vowels in that string??

s="shrirampur"
v="aeiouAIEOU"
cnt=0
for ch in s:
    if ch in v:
        cnt=cnt+1
print("Counted Vowel=",cnt)
