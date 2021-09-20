#If you have a list of 99 numbers, 1-100 with one number missing (e.g. 67) write an algorithm to find the missing number.



test = list(range(1,101))

test[76] = 0

print(test)

sum100 = sum(range(1,101))

print(sum(range(1,101)) - sum(test))