events_count=([1,2,4,8,9,10])
def words_count():
    N=0
    for i in range(6):
        if events_count[i]%2==0:
            N=N+1
    return print(N)
words_count()
    
