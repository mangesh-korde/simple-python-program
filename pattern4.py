# Generate the pattern..
''' * * * * *
      * * * *
        * * *
          * *
            *
'''

for i in range(5,0,-1):
    print(" "*(5-i),end="")
    print("*"*i)
