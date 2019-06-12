def partition_odd_even(mylist):
    even=[]
    odd=[]
    for i in range(len(mylist)):
        if mylist[i]%2==0:
            even.append(mylist[i])
        else:
            odd.append(mylist[i])
    return print(odd,even)



def add_ending(mylist,ending):
    new=[]
    for i in range(len(mylist)):
        new.append(mylist[i]+ending)
    return print(new)

partition_odd_even([1, 2, 3, 4, 5])
add_ending(["clever", "meek", "hurried", "nice"], "ly")
