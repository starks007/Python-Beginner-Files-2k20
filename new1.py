a=input("Enter encoded message")
b=""
c=""
for i in a:
    b=i+b
for i in b:
    if ((i.isalpha())==True):
        c=c+i
    elif (i==' '):
        c=c+' '
print (c)

           
