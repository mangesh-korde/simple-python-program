#Q...write a python program that accepts hyphen-separated
#    sequence of words as input and prints the  words in a hyphen
#    separated sequence after sorting them alphabetically???

s="green-red-yellow-black-white"
s1=s.split("-")
s1.sort()
for val in s1:
    print(val,end="-")

