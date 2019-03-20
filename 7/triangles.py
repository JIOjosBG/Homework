x=int(input("a"))
y=int(input("b"))
z=int(input("c"))
if x==y and y==z:
    print("ravnostr")
elif x==y or y==z or z==x:
    print("ravnobedren")
else:
    print("raznostranen")