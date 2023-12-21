def sum_of_divisors_in_range(N):
    if N < 50 or N > 84:
        return 0
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            if i < 50 or i > 84:
                continue
            ans += i
    return ans
