




def missing_letters(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for c in alphabet:
        if c not in string:
            print(c)
    

import string
  
alphabet = set(string.ascii_lowercase)
  
def ispangram(string):
    print(set(string.lower()))
    print(alphabet)
    return set(string.lower()) >= alphabet

test = "the quick brown fox jumps over the lazy dog"

missing_letters(test)
# print(ispangram(test))