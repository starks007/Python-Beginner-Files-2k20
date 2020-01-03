#user enters a number of elements from which it shows the sum of the even elements

n=int(input("enter"))
a=[]
su=0
for i in range (0,n):
    ele=int(input("enter"))
    a.append(ele)
for i in range(0,n):
    if (a[i]%2==0):
        su=su+a[i]
print (a)
print (su)
