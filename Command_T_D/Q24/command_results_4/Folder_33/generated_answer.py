def sum_of_divisors_in_range(n):
    l, r = 157, 902
    while l <= r:
        m = l + r >> 1
        if m == n or m == n // 2 or n % m == 0:
            return 1 + sum(range(n, n//2, -1))
        elif n % m == 1:
            return 0
        l += 1
        r -= 1
    return 0
