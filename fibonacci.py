def fibonacci(n):
    b=0
    a=1
    print("0")
    print("1")
    while n!=0:    
        c=a
        a=a+b
        b=c
        n=n-1
        print (a)
n=int(input("ENTER THE NUMBER OF FIBONACCI SEQUENCE YOU WANT"))
if n==0:
    print("0")
elif n==1:
    print("1")
elif n==2:
    print("1")
else:
    fibonacci(n)


    
            
    
