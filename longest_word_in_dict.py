# Given a dictionary of words and a string of characters, find the longest word or words that contain\
# all the characters in the list of characters. If there are more than one matching word 
# of the same length in the dictionary, all of them should be returned. 
# Example:
# dictionary ("ban", "car" "banana")
# string "annaab"
# Should return ["banana"]

# O(N*(K+n)) Here N is the length of dictionary and n is the length of given string ‘str’ and K – maximum length of words in the dictionary.

def isSubSequence(str1, str2):
 
    m = len(str1)
    n = len(str2)
 
    j = 0; # For index of str1 (or subsequence
 
    # Traverse str2 and str1, and compare current
    # character of str2 with first unmatched char
    # of str1, ifmatched then move ahead in str1
    i = 0
    while (i < n and j < m):
        print(str1[j], str2[i])
        if (str1[j] == str2[i]):
            j += 1
        i += 1
 
    # If all characters of str1 were found in str2
    return (j == m)


def findLongestString(words, string):
    result = ""
    length = 0
    print(string)
 
    # Traverse through all words of dictionary
    for word in dict1:
        print(word)
        # If current word is subsequence of str and is largest
        # such word so far.
        if (length < len(word) and isSubSequence(word, str1)):
            result = word
            length = len(word)
    # Return longest string
    return result
 

dict1 = ["ale", "apple"] #,"monkey", "plea"]
str1 = "abpcplea" 
print(findLongestString(dict1, str1))