num=int(input("enter a number! "))
i=1
c=0
sum=0
while i<=num:
    if i%2!=0:
        sum+=i
        c+=1
        print(i,"odd number ")
    i+=1 
print(c,"total count")
print(sum)
