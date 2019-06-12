def is_symmetrical(n):
    if len(str(n))%2==0:
        for i in range(int(len(str(n))/2)):
            if str(n)[i] != str(n)[(-1)*(i+1)]:
                return print("False")
        return print("True")
    else:
        for i in range(int(len(str(n))/2)):
            if str(n)[i] != str(n)[(-1)*(i+1)]:
                return print("False")
        return print("True")

def is_valid_pin(n):
    nums=["1","2","3","4","5","6","7","8","9","0"]
    if str(n)==n:
        if len(n)==4 or len(n)==6:
            for i in n:
                if (i in nums) != True:
                    return print("False")
            return print("True")
        else:
            return print("False")

    return print("Must be string")

def longest_zero(n):
    count=0
    best=0
    if str(n)==n:
        for i in range(len(n)):
            if count>=best:
                best=count
            if n[i]=="0":
                count+=1
            else:
                count=0
        return print("\"","0"*best,"\"")

    return print("Must be string")

def get_extension(name):
    ext=[]
    on=False
    if str(name)==name:
        for i in range(len(name)):
            if on:
                ext.append(name[i])
            if name[i]==".":
                on=True
        return print("".join(ext))

    return print("Must be string")

def sum_digits(a,b):
    all=[]
    sum=0
    for i in range((b-a)+1):
        all.append(a+i)
    for i in range(len(all)):
        for j in str(all[i]):
            sum+=int(j)

    return print(sum)


is_symmetrical(1221)
is_valid_pin("1234")
longest_zero("01100001011000")
get_extension("code.html")
sum_digits(10, 12)
