num=int(input("num="))
def change(num):
    print("it is")
    if num>=100:
        print(int((num-num%100)/100),"* 100")
        num=num%100
    if num>=50:
        print(int((num-num%50)/50),"* 50")
        num=num%50
    if num>=20:
        print(int((num-num%20)/20),"* 20")
        num=num%20
    if num>=10:
        print(int((num-num%10)/10),"* 10")
        num=num%10
    if num>=5:
        print(int((num-num%5)/5),"* 5")
        num=num%5
    if num>=2:
        print(int((num-num%2)/2),"* 2")
        num=num%2
    if num>0:
        print(num,"*1")

change(num);
