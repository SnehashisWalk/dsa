'''
Problem - Can Sum
Write a function canSum(targetSum, nums) that takes in a targetSum and an array of numbers as args

The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array

An element of the array can be used as many times as needed

Assume all numbers are positive
'''
import time
# brute force - time - O(n^m); n = len(nums), m = targetSum
def canSum(targetSum, nums):
    if targetSum == 0: return True
    if targetSum < 0: return False
    for i in nums:
        remainder = targetSum - i
        if canSum(remainder, nums):
            return True
    return False

# curr = time.time()
# print(canSum(7, [2, 3]))
# print(canSum(7, [5, 3, 4, 7]))
# print(canSum(7, [2, 4]))
# print(canSum(8, [2, 3, 5]))
# print(canSum(300, [7, 14]))
# print('time elapsed: ', time.time() - curr)

# memoization
# Time - O(n * m); n = len(nums), m = targetSum
def canSumMemo(targetSum, nums, memo=None):
    if memo is None: memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True 
    if targetSum < 0: return False
    for i in nums:
        remainder = targetSum - i
        if canSumMemo(remainder, nums, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

curr = time.time()
print(canSumMemo(7, [2, 3]))
print(canSumMemo(7, [5, 3, 4, 7]))
print(canSumMemo(7, [2, 4]))
print(canSumMemo(8, [2, 3, 5]))
print(canSumMemo(300, [7, 14]))
print('time elapsed: ', time.time() - curr)