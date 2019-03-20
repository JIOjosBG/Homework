num=int(input("num="))
def NumDigitCount(num):
    if num<10:
        DigitCount=1
    elif num<100:
        DigitCount=2
    else:
        DigitCount=3
    return DigitCount
def OnesToText(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'
def TeensToText(num):
    if num==11:
        return 'eleven'
    elif num==12:
        return 'twelve'
    elif num==13:
        return 'thirteen'
    elif num==14:
        return 'fourteen'
    elif num==15:
        return 'fifteen'
    elif num==16:
        return 'sixteen'
    elif num==17:
        return 'seventeen'
    elif num==18:
        return 'eighteen'
    elif num==19:
        return 'nineteen'
def TensToText(num):
    if num==10:
        return 'ten'
    elif num==20:
        return 'twenty'
    elif num==30:
        return 'thirty'
    elif num==40:
        return 'fourty'
    elif num==50:
        return 'fifty'
    elif num==60:
        return 'sixty'
    elif num==70:
        return 'seventy'
    elif num==80:
        return 'eighty'
    elif num==90:
        return 'ninety'
def HundredsToText(num):
    if num==100:
        return 'onehundred'
    elif num==200:
        return 'twohundred'
    elif num==300:
        return 'threehundred'
    elif num==400:
        return 'fourhundred'
    elif num==500:
        return 'fivehundred'
    elif num==600:
        return 'sixhundred'
    elif num==700:
        return 'sevenhundred'
    elif num==800:
        return 'eighthundred'
    elif num==900:
        return 'ninehundred'
def NumToText(num):
    if NumDigitCount(num)==1:
        return OnesToText(num)
    elif NumDigitCount(num)==2 and num%10==0:
        return TensToText(num)
    elif NumDigitCount(num)==2 and num<20:
        return TeensToText(num)
    elif NumDigitCount(num)==2 and num%10!=0:
        return TensToText(num-num%10),OnesToText(num%10)
    elif NumDigitCount(num)==3:
        if num%100==0:
            return HundredsToText(num)
        elif num%10==0:
            return HundredsToText(num-num%100),'and',TensToText(num%100)
        elif num%100<10:
            return HundredsToText(num-num%100),'and',OnesToText(num%100)
        elif num%100<20:
            return HundredsToText(num-num%100),'and',TeensToText(num%100)
        elif num%10!=0:
            return HundredsToText(num-num%100),'and',TensToText(num%100-num%10),OnesToText(num%10)
print(NumToText(num))
#for i in range(999):
#   print(NumToText(i))
        