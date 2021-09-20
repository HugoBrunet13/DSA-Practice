
#Given a string , transform It and return a string so that aabbcc -> a2b2c2 , abb -> a1b2 ,  aaba -> a2b1a1


def transform_string(s):

    i = 0
    final_str=''

    while(i < len(s)-1):
        cpt = 1
        while(i <  len(s)-1 and s[i] == s[i + 1]):
            print(s[i])
            i  += 1
            cpt += 1
        final_str += s[i] + str(cpt)
        i += 1
    return final_str


st = "wwwwaaadexxxxxxywww"
transform_string(st)
