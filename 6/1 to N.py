n=int(input("N?"))
chetni=bool(input("chetni li?"))
a=0
for i in range(n):
    if chetni:
        if i%2==0:
            a=a+i
    if chetni==False:
        if i%2==1:
            a=a+i
print(a)
