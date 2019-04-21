a=int(input())
b=input().split()
for i in range(a):
   b.insert(i,int(b[i]))
   
   b.remove(b[i+1])

b.sort()
print(b[0])


