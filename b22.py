a=int(input("enter the number:"))
b=input().split()
for i in range(a):
   b.insert(i,int(b[i]))
   
   b.remove(b[i+1])

b.sort(reverse=True)
print(b[0])
