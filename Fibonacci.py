memo = {0: 0, 1: 1}
def Fibo(num: int) -> int :
    if num not in memo:
        memo[num] = Fibo(num-1) + Fibo(num-2)
    return memo[num]