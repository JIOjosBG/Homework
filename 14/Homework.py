def count_words(words):
    wordsCount=dict()
    for i in range(len(words)):
        wordsCount[words[i]]=words.count(words[i])

    return print(wordsCount)


def count_vowels_consonants(word):
    wordlist=list(word)
    worddict=dict()
    worddict['vowels']=0
    worddict['consonants']=0
    for i in range(len(wordlist)):
        if wordlist[i]=='a' or wordlist[i]=='e' or wordlist[i]=='i' or wordlist[i]=='o' or wordlist[i]=='u' or wordlist[i]=='y' or wordlist[i]=='A' or wordlist[i]=='E' or wordlist[i]=='I' or wordlist[i]=='O' or wordlist[i]=='U' or wordlist[i]=='Y':
            worddict['vowels']=worddict['vowels']+1
        else:
            worddict['consonants']=worddict['consonants']+1
    return print(worddict)


def status_count(students):
    finalizedStudents=dict()
    finalizedStudents['finalized']=list(range(len(students)))
    finalizedStudents['not_finalized']=list(range(len(students)))
    for i in range(len(students)):
        if students[i]['status']=='finalized':
            finalizedStudents['finalized'][i]=students[i]['name']
        else:
            finalizedStudents['not_finalized'][i]=students[i]['name']
    #for i in range(len(students)):
        #if i < len(finalizedStudents['finalized']):
            #if finalizedStudents['finalized'][i] in range(len(students)):
                #finalizedStudents['finalized'].pop(i)
        empety={0:' ','finalized':0,'not_finalized':0}
    for i in range(len(finalizedStudents['finalized'])):
        for j in range(len(finalizedStudents['finalized'])):
            if finalizedStudents['finalized'][i]==j:
                finalizedStudents['finalized'][i]=empety[0]
                
    for i in range(len(finalizedStudents['not_finalized'])):
        for j in range(len(finalizedStudents['not_finalized'])):
            if finalizedStudents['not_finalized'][i]==j:
                finalizedStudents['not_finalized'][i]=empety[0]
            
    for i in range(len(finalizedStudents['finalized'])):
        if i<len(finalizedStudents['finalized']):
            if finalizedStudents['finalized'][i]==empety[0]:
                finalizedStudents['finalized'].pop(i)
                finalizedStudents['finalized'].insert(0,empety[0])
                
    for i in range(len(finalizedStudents['not_finalized'])):
        if i<len(finalizedStudents['not_finalized']):
            if finalizedStudents['not_finalized'][i]==empety[0]:
                finalizedStudents['not_finalized'].pop(i)
                finalizedStudents['not_finalized'].insert(0,empety[0])
    for i in range(len(finalizedStudents['finalized'])):
        if finalizedStudents['finalized'][i]==empety[0]:
            empety['finalized']=empety['finalized']+1
        if finalizedStudents['not_finalized'][i]==empety[0]:
            empety['not_finalized']=empety['not_finalized']+1
    for i in range(empety['finalized']):
        finalizedStudents['finalized'].pop(0)
    for i in range(empety['not_finalized']):
        finalizedStudents['not_finalized'].pop(0)
    return finalizedStudents
                
students = [
         {
             "name": "RadoRado",
             "status": "not_finalized"
         },
         {
             "name": "Ivo",
             "status": "finalized"
         },
         {
             "name": "Genadi",
             "status": "finalized"
         }
     ]
#status_count(students)
