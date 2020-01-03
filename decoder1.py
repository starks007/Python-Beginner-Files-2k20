#Enter the encoded message from the message generator to decode the message it has some issues
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
