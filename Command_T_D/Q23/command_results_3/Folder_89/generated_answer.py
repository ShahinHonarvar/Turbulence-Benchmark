import heapq as hq
def find_divisors_in_range(n):
    res = []
    l, r = 1, n//2
    divisor = 1
    while l <= r:
        while divisor * l <= n:
            divisor += 1
            if divisor > 14:
                break
            if divisor not in res:
                res.append(divisor)
        l += 1
    return res
