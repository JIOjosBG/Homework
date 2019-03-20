a=int(input("sizze?"))
b=1
for i in range(a):
    for j in range(b):
        print("*", end =" ")
    print("\n")
    if b<=a:
        b=b+1
