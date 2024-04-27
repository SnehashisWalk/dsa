# Grid traveler - find the min path from S to E
#   S _ _
#   _ _ _
#   _ _ E
import time

# Time: O(2 ^ (m + n))
def gridTraveler(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

curr = time.time()
print(gridTraveler(1,1)) #1
print(gridTraveler(2,3)) #3
print(gridTraveler(3,2)) #3
print(gridTraveler(3,3)) #6
print(gridTraveler(8,8))
print('Time elapsed: ', time.time() - curr)
# with memoization
# time O(m*n)
def gridTraveler(m, n, memo = {}):
    key = f'{m},{n}'
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]

print('with memoization')
curr = time.time()
print(gridTraveler(1,1)) #1
print(gridTraveler(2,3)) #3
print(gridTraveler(3,2)) #3
print(gridTraveler(3,3)) #6
print(gridTraveler(8,8))
print('Time elapsed: ', time.time() - curr)