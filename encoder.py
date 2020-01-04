import random
c=''
a=input('Enter the message')
length=len(a)
for i in range(length-1,-1,-1):
    l=random.randrange(2,5)
    for j in range (0,l):
        b=random.randrange(0,9)
        b=str(b)
        c=c+b
    c=c+a[i]
print (c)
input('')
        
