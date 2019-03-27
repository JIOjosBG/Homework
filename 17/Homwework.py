alphabet="abcdefghijklmnopqrstuvwxyz"
def encrypt(text, key):
    resoult=list(range(len(text)))
    for i in range(len(text)):
            resoult[i]=alphabet[(alphabet.index(text[i])+key)%26]
    resoult=''.join(resoult)
    return print("you entered ",text," encrypted with ",key," it is ",resoult)  
encrypt('zalphabet', int(input("Encript with ")))


def decrypt(text,key):
    resoult=list(range(len(text)))
    for i in range(len(text)):
            resoult[i]=alphabet[(alphabet.index(text[i])-key)%26]
    resoult=''.join(resoult)
    return print("you entered ",text,"decripred with ",key," it is ",resoult)  
decrypt('zalphabet', int(input("Decrypt with ")))

def decode_word(encrypted_word, cipher):
    resoult=list(range(len(encrypted_word)))
    for i in range(len(encrypted_word)):
        resoult[i]=cipher[encrypted_word[i]]
    return print(resoult)

print("\n to use the function encode_word type encode_word('your word','dict with information about how to decode it')")

decode_word("mjriew", {'i': 'h', 'j': 'y', 'e': 'o', 'r': 't', 'w': 'n', 'm': 'p'})
