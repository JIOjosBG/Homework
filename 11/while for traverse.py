books = ["Learn You a Haskell",
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"
         "\n"]
def for_traverse():
    for i in range(len(books)):
        print(books[i])
        
def while_traverse(i):
    while i <=len(books)-1:
        print(books[i])
        i=i+1
    
for_traverse()
while_traverse(0)
