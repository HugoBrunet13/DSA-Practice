from collections import Counter, defaultdict

import datetime

def get_first_non_repeating_char_optimized(string) :
    counter = Counter(string) # get hashmap with letter of string as key, and the number of occurence as value
    for c in string:
        if counter[c] == 1:
            return c
    return False


def get_first_non_repeating_char(string) :
    counter = {}
    for c in string:
        counter[c] = counter.get(c, 0) + 1
    # print(counter)
    for c in string:
        if counter[c] == 1:
            return c
    return False

string = "geeksforgeeks"


start=datetime.datetime.now()
print(get_first_non_repeating_char(string))
end=datetime.datetime.now()
print("exec time: %s"%(end - start))

start=datetime.datetime.now()
print(get_first_non_repeating_char_optimized(string))
end=datetime.datetime.now()
print("exec time: %s"%(end - start))



a = [1,2,3.5,6,2,8,4,7,9,3]

print(defaultdict(int))