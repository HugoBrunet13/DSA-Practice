def distance(string, w1, w2):
    if w1 == w2:
        return 0

    string = string.split() # put string into list of words

     # assume total length of the string as
    # minimum distance
    min_dist = len(string)+1

    # get first place of first occurence
    first_pos = None
    for i in range(0, len(string)):
        if string[i] == w1 or string[i] == w2:
            first_pos = i
            break 
    if first_pos is None:
        return False

    # travers string starting from first occurence:
    while (i < len(string)):
        print("i: %s, first_pos: %s" %(i, first_pos))   
        if string[i] == w1 or string[i] == w2:

            if (string[first_pos] != string[i] and (i - first_pos) < min_dist):
                print(string[i])
                min_dist = i - first_pos - 1
                first_pos = i
            else:
                print("in else: ", string[i])
                first_pos = i
        i += 1

    return min_dist


s = "yo yo yo yo geeks for geeks contribute test geeks tesh blbabla practice bla bla bla geeks test7 practice"
w1 = "geeks"
w2 = "practice"
print(distance(s, w1, w2))




    