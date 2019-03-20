words=["one","two","three","four","one"]
word="one"
def words_count(words,word):
    count_of_words=0
    for i in range(len(words)):
        if words[i]==word:
            count_of_words+=1
    return print("the list is",words," \n the word is ",word,"\n the word was found",count_of_words,"time/s")
            
words_count(words,word)
