##########A=[]
##########for v in range(1,5):
##########    A.append(int(input("Enter number : ")))
##########print(A)
##########
##########def buble(A):
##########    l = len(A)
##########    for i in range(1,l):
##########        for j in range(1,l-i+1):
##########            if(A[j] < A[j-1]):
##########                A[j] , A[j-1] = A[j-1] , A[j]
##########
##########buble(A)
##########print("sorted array")
##########print(A)
##########        
########
########
########x=[]
########for i in range(1,5):
########    x.append(int(input("enter a number : ")))
########print(x)
########
########def buble(x):
########    l = len(x)
########    for p in range(1,l):
########        for j in range(1,l-p+1):
########            if(x[j] < x[j-1]):
########               x[j],x[j-1] = x[j-1],x[j]
########
########print("sorted array")
########buble(x)
########print(x)
######
######A=[]
######for k in range(1,6):
######    A.append(float(input("enter float number - ")))
######print(A)
######
######def bub(A):
######    ln = len(A)
######    for i in range(1,ln):
######        for j in range(1,ln-i+1):
######            if(A[j] < A[j-1]):
######                A[j],A[j-1] = A[j-1],A[j]
######
######print("sorted array")
######bub(A)
######print(A)
######
######
######
######
######
####
####
####x=[]
####for k in range(1,5):
####    x.append(float(input("enter the number - ")))
####print("Entered numbers")
####print(x)
####
####def bub(x):
####    ln = len(x)
####    for i in range(1,ln):
####        for j in range(1,ln-i+1):
####            if(x[j]<x[j-1]):
####                x[j-1],x[j] = x[j],x[j-1]
####
####print("sordetd order")
####bub(x)
####print(x)
####
####
####
####
####
####
####
####
####insertion sort
##
####a=[]
####n=9
####for i in range(0,n):
####    num = int(input("enter the number"))
####    if(num>10 and num<20):
####         a.append(num)
####    else:
####         print("error")
####print(a)
####
####def insertion(a):
####    for i in range(1,len(a)):
####        key = a[i]
####        j=i-1
####        while j>=0 and key<a[j]:
####            a[j+1]=a[j]
####            j=j-1
####        a[j+1] = key
####
####insertion(a)
####print(a)
##
##a=[]
##n=5
##for i in range(0,n):
##    num = int(input("enter number"))
##    if(num>1 and num<20):
##        a.append(num)
##    else:
##        print("error")
##
##def ins(a):
##    for i in range(1,len(a)):
##        key=a[i]
##        j=i-1
##        while j>=0 and key<a[j]:
##            a[j+1]=a[j]
##            j=j-1
##            a[j+1] = key
##
##ins(a)
##print(a)
##


a=[]
n=5
for i in range(0,n):
    num = int(input("enter"))
    if(num>2 and num<10):
        a.append(num)
    else:
            print("eror")

def ins(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=key

ins(a)
print(a)
