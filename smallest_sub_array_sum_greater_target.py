    # Given an array, find a subarray such the sum of the elements in 
    # subarray is greater than or equal to target value. Find the minimum length of such subarray.


def minSubArrayLen(target, nums):
        left = total = 0
        res = len(nums) + 1
        print(nums)
        for i in range(len(nums)):
            print("Total: %s, nums[i]: %s"%(total, nums[i]))
            total = total + nums[i]
            print("New total: %s" %total)
            while total >= target:
                print("here")
                res = min(res,i-left+1)
                total = total - nums[left]
                left = left+1
        return res if res <= len(nums) else 0

 
# Driver program
nums = [2,3,1,2,4,3]
target = 7
res1 = minSubArrayLen(target, nums)
print(res1)
