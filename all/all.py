
numbers = [1, 5, 3,  -1, 2]
def max(numbers):
    nowmax=numbers[0]
    for i in range(len(numbers)):
        if nowmax<numbers[i]:
            nowmax=numbers[i]
            index=i
    return nowmax,i
max_number = max(numbers)
print(max_number)


numbers = [123, 100, 345, 200, 5, 500]
def num(numbers):
    new=list(range(len(numbers)))
    print(new)
    for i in range(len(new)):
        new[i]=0
        nulls=0
    for i in range(len(numbers)):
        if numbers[i]%100==0:
            new[i]=numbers[i]
        else:
            nulls=nulls+1
    for i in range(nulls):
        new.remove(0)
    return new
            
            
print(num(numbers))
        
        
       

numbers = [1, 5, 3,  -1, 2]
print(numbers[0])
print(numbers[2])
print(numbers[-1])


numbers = [1, 0, 3, 5, 0, 2]
numbers.remove(numbers[1])
numbers.remove(numbers[3])
print(numbers)

"""Код, за премахване на нулите"""

def nozeros(numbers):
    nulls=0
    for i in range(len(numbers)):
        if numbers[i]==0:
            nulls=nulls+1;
    for i in range(nulls):
        numbers.remove(o)
    return numbers

text = 'ab m'
def has_spaces(text):
    if ' ' in text:
        print(True)
    else:
        print(False)
has_spaces(text)


n  = 5
def make_dashed_sttring(n):
    print(n * "-")
make_dashed_sttring(n)




text = "xyz1pq2"
c = '0123456789'

def digits_count(text,c ):
    a=0
    for item in text:
        if item in c:
            a = a + 1
    return print(a)
digits_count(text,c)


text='my text'
vowels='eyuioa'
def first_vowel_index(text,vowels):
    for i in range(len(text)):
        for j in range(len(vowels)):
            if text[i]==vowels[j]:
                return i
print(first_vowel_index(text,vowels))



def word_count(text):
    spaces=0
    for i in range(len(text)):
        
        if text[i]== ' ':
            spaces=spaces+1
    return spaces+1
print(word_count(text))

def vowels_to_upper(text,vowels):
    new=list(range(len(text)))
    for i in range(len(text)):
        new[i]=0
    for i in range(len(new)):
        for j in range(len(vowels)):
            if text[i]==vowels[j]:
                new[i]=1
    for i in range(len(new)):
        if new[i]!=1:
            new[i]=text[i]
        else:
            new[i]=text[i].upper()
    new="".join(new)
            
                
    return new
print(vowels_to_upper(text,vowels))
                
num=[[1, 2, 3],[3, 2, 1]]

def ones_count(numbers):
    ones=0
    for i in range(len(num)):
        for j in range(len(num[i])):
            if num[i][j]==1:
                ones=ones+1
    return ones

print(ones_count(num))


def same_case(letter1, letter2):
    if letter1.upper==letter1 and letter2.upper==letter2:
        return print(True)
    elif letter1.upper!=letter1 and letter2.upper!=letter2:
        return(print(True))
    else:
        return print(False)

same_case("A", "B")
not same_case("A", "a")

def equal_no_case(letter1, letter2):
    if letter1.upper()==letter2.upper():
        print(True)
    else:
        print(False)

equal_no_case("A", "a")
not equal_no_case("A", "B")