def pascal_triangle(x):
    values=list(range(x))
    for i in range(x):
        values[i]=list(range(i+1))
        for j in range(i+1):
            values[i][j]=1
            if i==0 or j==0 or j==i or i==0:
                values[i][j]=1
            else:
                values[i][j]=values[i-1][j-1]+values[i-1][j]
                        
    


            
    for i in range(x):
        print(" " * 2*(x-i) , values[i])
print(pascal_triangle(10))
