

def find_cheapest_price_time_interval(intervals):


    startTimes = [i[0] for i in intervals]
    endTimes = [i[1] for i in intervals]

    all_times = startTimes + endTimes 
    all_times.sort()
    
    all_ranges = []
    for i in range(0, len(all_times)-1):
        all_ranges.append([all_times[i], all_times[i+1], 0])

    
    for j in range(0, len(all_ranges)):
        r = all_ranges[j]
        res = 0
        for i in intervals:
            if r[0] >= i[0] and  r[1] <= i[1]:
                if not res:
                    res = i[2]
                elif i[2] < res:
                    res = i[2]
        r[2] = res
        

    return [ interval for interval in all_ranges if interval[2] != 0]

    

arr = [
    [1,5,15], 
    [2,3,10],
    [4, 8, 18]
]

arr2 = [
    [0,4,5], 
    [2,8,3],
    [7, 11, 10]
]

arr3 = [
    [0,8,5], 
    [2,4,3],
    [7, 11, 10]
]

# 1,2, 15
# 2, 3, 10
# 3, 5, 15
#5, 8
# 3, 5, 15
# 5, 8 18
print(find_cheapest_price_time_interval(arr))
print(find_cheapest_price_time_interval(arr2))
print(find_cheapest_price_time_interval(arr3))