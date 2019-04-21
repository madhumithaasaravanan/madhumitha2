n=int(input("Enter the number:"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("Yes")
else:
    print("No")
