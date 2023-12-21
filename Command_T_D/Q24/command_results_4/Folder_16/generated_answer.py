def sum_of_divisors_in_range(n):
    a, b = 228, 846
    if n < a or n > b:
        return 0
    ans = 0
    for i in range(a, b + 1):
        if n % i == 0:
            ans += i
    return ans
