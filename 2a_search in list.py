list=[]
numbers=int(input("enter the list length"))
print("enter numbers")
for i in range(numbers):
    data=int(input())
    list.append(data)    
print(list)
search = int(input("ENTER NUMBER YOU WANT TO SEARCH"))
if search in list:
    
    print(search,"FOUND")
else:
    print(search,"NOT FOUND")

