def rev1(str):
    list= str.split();
    list.reverse()
    print(" ".join(list))
def rev2(str):
    list=str.split()
    str2=" "
    for i in list:
        str2+=i[::-1]
        str2+=" "
    print(str2)
str=input("ENTER WHICH word YOU WANT TO reverse")
rev1(str)
rev2(str)
