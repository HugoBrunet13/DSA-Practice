'''
Given a 2-D String array of student-marks find the student with the highest average and output his average score. If the average is in decimals, floor it down to the nearest integer.

Example 1:
----------
Input:  [9"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]
Output: 99
Explanation: Since Jessica's average is greater than Bob's, Mike's and Jason's average.
'''

def maxAvgScore(scores):
    hashmap = {}

    for name, score in scores:
        if name in hashmap:
            hashmap[name].append(int(score))
        else:
            hashmap[name] = [int(score)]

    max_score = 0
    for i in hashmap:
        avg =  sum(hashmap[i]) / len(hashmap[i]) 
        max_score = avg if avg > max_score else avg
    
    return max_score



    # return 0

scores = [["Bob","87"], ["Mike", "35"],["Bob", "52"], ["Jason","35"], ["Mike", "55"], ["Jessica", "99"]]
print(maxAvgScore(scores))