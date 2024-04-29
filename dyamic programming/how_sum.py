'''
Problem - How Sum
Write a function howSum(targetSum, nums) that takes in a targetSum and an array of numbers as args

The function should return an array containing any combination of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return null.

If there are multiple combinations possible you may return any single one.
'''
import time

# brute force - time - O((n^m) * m); n = len(nums), m = targetSum
def howSum(targetSum, nums):
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    for num in nums:
        remainder = targetSum - num
        result = howSum(remainder, nums)
        if result is not None:
            result.append(num)
            return result
    
    return None

curr = time.time()
print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
# print(howSum(300, [7, 14]))
print('time elapsed: ', time.time() - curr)

# memoization
# Time - O(n * m * m); n = len(nums), m = targetSum

def howSumMemo(targetSum, nums, memo=None):
    if memo is None: memo = {}
    
    if targetSum in memo: return memo[targetSum]
    
    if targetSum == 0: return []
    
    if targetSum < 0: return None
    
    for num in nums:
        remainder = targetSum - num
        result = howSumMemo(remainder, nums, memo)
        if result is not None:
            memo[targetSum] = result + [num]
            return memo[targetSum]
    
    memo[targetSum] = None
    return None

print('Memoized')
curr = time.time()
print(howSumMemo(7, [2, 3]))
print(howSumMemo(7, [5, 3, 4, 7]))
print(howSumMemo(7, [2, 4]))
print(howSumMemo(8, [2, 3, 5]))
# print(howSum(300, [7, 14]))
print('time elapsed: ', time.time() - curr)