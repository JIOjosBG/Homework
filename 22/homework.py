def rook_can_capture(pos1, pos2):
    if str(pos1)==pos1 and str(pos2)==pos2 and len(pos1)==2 and len(pos2)==2:
        if pos1[0]==pos2[0]:
            return print(True)
        elif pos1[1]==pos2[1]:
            return print(True)
    return print(False)

def  filter_by_digit_length(mylist, n):
    new=[]
    for i in range(len(mylist)):
        if len(str(mylist[i]))==n:
            new.append(mylist[i])
    return print(new)

def test_jackpot(mylist):
    same=True
    sameas=mylist[0]
    for i in range(len(mylist)):
        if mylist[i]==sameas:
            same=True
        else:
            same=False
    return print(same)


def sub_reddit(string):
    name=list()
    toberemoved="https://www.reddit.com/r/"
    for i in range(len(string)):
        name.append(string[i])
    for i in range(len(toberemoved)):
        del name[0]
    del name[-1]
    name="".join(name)
    return print(name)

def findme(str,item):
    for i in range(len(str)):
        if str[i]==item:
            return i



def removelast(mylist,item):
    while  (mylist[-1]==item):
        mylist.pop(-1)
    return mylist



def percent_to_decimal(mystring):
    result=list()
    for i in range(len(mystring)):
        result.append(mystring[i])
    del result[-1]
    #result="".join(result)
    #result=float(result)
    whereisdot=findme(result,".")
    if whereisdot==None:
        if len(result)==1:
            result.insert(0,"0")
            result.insert(0,".")
            result.insert(0,"0")
        elif len(result)==2:
            result.insert(0,".")
            result.insert(0,"0")
        elif len(result)>=3:
            result.insert(-2,".")
    elif whereisdot==1:
        result.remove(".")
        result.insert(0,"0")
        result.insert(0,".")
        result.insert(0,"0")
    elif whereisdot==2:
        result.remove(".")
        result.insert(0,".")
        result.insert(0,"0")
    elif whereisdot>=3:
        result.remove(".")
        result.insert(whereisdot-2,".")


    result=removelast(result,"0")

    if result[-1]==".":
        result.pop(-1)
    result="".join(result)

    #result.insert(0, ".")
    return print(result)



rook_can_capture("A8", "E8")
filter_by_digit_length([123, 3456, 1, 68, 789], 3)
test_jackpot(["$", "$", "$", "$", "$"])
sub_reddit("https://www.reddit.com/r/funny/")
percent_to_decimal("10.1%")
