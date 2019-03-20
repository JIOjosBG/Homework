s=str(input("your word is "))
def all_caps(s):
    count=0
    areAllCaps=True
    for i in range(len(s)):
        if s[i]==s[i].upper():
            count=count+1
    if len(s)==0:
        return print("You didint write anything")
    if count!=len(s):    
        return print("Not all caps")
    else:
        return print("All caps")
all_caps(s)

def caps_count(s):
    count=0
    for i in range(len(s)):
        if s[i]==s[i].upper():
            count=count+1
    return print("The count of the caps is",count)
caps_count(s)

def cons_count(s):
    count=0
    areAllCaps=True
    for i in range(len(s)):
        if s[i].upper()!="A" and s[i].upper()!="I" and s[i].upper()!="E" and s[i].upper()!="O" and s[i].upper()!="U" and s[i].upper()!="Y":
            count=count+1    
    return print(count,"consonants here")
cons_count(s)

stc='snake_to_camel'
def snake_to_camel(stc):
    count=0
    save=list(range(len(stc)))
    for i in range(len(stc)):
        if i!=0:
            if stc[i-1]=="_":
                save[i]=stc[i].upper()
            else:
                save[0]=stc[0]
                save[i]=stc[i]
            
        if save[i]=="_":
            count=count+1
    for i in range(count):
        save.remove("_")
    return print(stc,"\n",save)
snake_to_camel(stc)

stp='snake_to_pascal'
def snake_to_pascal(stp):
    count=0
    save=list(range(len(stp)))
    for i in range(len(stp)):
        if i!=0:
            if stp[i-1]=="_":
                save[i]=stp[i].upper()
            else:
                save[0]=stp[0]
                save[i]=stp[i]
            
        if save[i]=="_":
            count=count+1
    for i in range(count):
        save.remove("_")
    save[0]=stp[0].upper()
    return print(stp,"\n",save)
snake_to_pascal(stp)

def avoids(word, forbidden_letters):
    lettersInWord=True
    for i in range(len(word)):
        for j in range(len(forbidden_letters)):
            if word[i]==forbidden_letters[j]:
                lettersInWord=False
    return print("your word is ",word,".Are the the letter/s ",forbidden_letters,"there:",lettersInWord)
avoids('program', 'abc')

def uses_only(word, letters):
    i=0
    onlyLetters=True
    ok=list(range(len(word)))
    for i in range(len(word)):
        for j in range(len(letters)):
            if word[i]==letters[j]:
                ok[i]=-1
    for i in range(len(ok)):
        if ok[i]!=-1:
            onlyLetters=False
    return print("Are there just the letters",letters,"in","word",word,":",onlyLetters)
uses_only('program', 'progam')

def uses_all(word, letters):
    i=0
    onlyLetters=True
    ok=list(range(len(letters)))
    for i in range(len(letters)):
        for j in range(len(word)):
            if letters[i]==word[j]:
                ok[i]=-1
    for i in range(len(ok)):
        if ok[i]!=-1:
            onlyLetters=False
    return print("All the letters from ",letters,"are used in ",word,":",onlyLetters)
uses_all('program', 'progam')

def volwels_count(s):
    count=0
    for i in range(len(s)):
        if s[i].upper()=="A" or s[i].upper()=="I" or s[i].upper()=="E" or s[i].upper()=="O" or s[i].upper()=="U" or s[i].upper()=="Y":
            count=count+1    
    return print("The count of the volwels is",count)
volwels_count(s)
