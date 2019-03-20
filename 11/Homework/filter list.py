def filter_list(a,b):
    c=a+b
    d=" "
    for i in range(len(c)):
        for j in range(len(c)):
            if i!=j:
                if c[i]==c[j]:
                    c[i]=" "
                    c[j]=" "
    for d in c:
        c.remove(" ")

    return print(c)
    
filter_list(['a','b','c'],['a'])
