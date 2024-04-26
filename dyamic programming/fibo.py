
def fib(n, memo):
    if memo[n] != 0: return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def main(n):
    memo = [0] * n
    memo[0] = memo[1] = 1
    print(fib(n-1, memo))
    print(memo)

main(5)

