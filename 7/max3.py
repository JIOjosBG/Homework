x=int(input("a"))
y=int(input("b"))
z=int(input("c"))
def max2(a,b):
    if a>b:
        return a;
    else:
        return b;
def max3(a,b,c):
    print(max2(max2(a,b),c))
max3(x,y,z)