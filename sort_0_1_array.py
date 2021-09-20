# If you have an array of 0s and 1s (e.g. [0,1,1,1,1,0,0,1,0,1,0,1,1] sort them so all the
# 1s are at the front of the array and all the zeros are at the back


def rearrange(arr):
    tot_1 = sum(arr)
    size_array = len(arr)

    tot_0 = size_array - tot_1

    return [1] * tot_1 + [0] * tot_0


test = [0,1,1,1,1,0,0,1,0,1,0,1,1] 

print(rearrange(test))