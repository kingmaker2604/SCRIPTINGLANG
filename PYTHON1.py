m=[]
k=0
n=int(input("enter number of elements:"))
for i in range(0,n):
    k=int(input("enter the element:"))
    m.append(k)
    i=i+1

m.sort()
print("minimum:")
print(m[0])
print("maximum:")
print(m[n-1])

m.append(8)
print(m)
m.remove(3)
print(m)

key=int(input("enter search element:"))
flag=0
for i in range(0,n):
    if(m[i]==key):
        flag=1
        break
    else:
        flag=0
        continue

if flag==1:
    print("element found")
else:
    print("element not found")
