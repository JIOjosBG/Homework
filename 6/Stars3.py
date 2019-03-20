a=int(input("size"))
b=1
c=False
for i in range(a*2-1):
    for j in range(b):
        print("*", end=" ")
    print("\n")
    if b==a:
        c=True
    if c==False:
        b=b+1
    if c==True:
        b=b-1
#a-brоi na \n
#b-brоi * na red
#c uvelichava li se briq * na red