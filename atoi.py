


# In Python, the ord() function accepts a string of unit length as an 
# argument and returns the Unicode equivalence of the passed argument. In other words, 
# given string of length 1, the ord() function returns an integer representing the Unicode code 
# point of the character when the argument is a Unicode object, or the value of the byte when the argument is an 8-bit string.

def isNumericChar(char) :
    if char >= '0' and char <= '9':
        return True
    return False


def myAtoi(string):
    if len(string) < 0:
        return False

    res = 0
    sign = 1 
    i = 0
    if string[0] == '-':
        sign = -1
        i += 1

    for j in range(i, len(string)):
        if not isNumericChar(string[j]):
            return False
        res = res * 10 + ord(string[j]) - ord('0')

    return res * sign


print(ord("3"))
print(ord("0"))


print(myAtoi('-100'))