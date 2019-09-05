n=int(input("ENTER A NUMBER FOR WHICH YOU WANT THE DIVISOR"))
for i in range (1,(n+1)):
    if(n%i==0):
        print(i,end=" ")
