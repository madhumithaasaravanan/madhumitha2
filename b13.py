x=int(input("enter the number:"))

for i in range (2,x):
    if x % i ==0:
        print("No")
        break
else:
    print("yes")
