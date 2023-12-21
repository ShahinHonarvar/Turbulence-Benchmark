def sum_of_divisors_in_range(n):
    if n < 27 or n > 44:
        return 0
    l, r = 1, n
    while l <= r:
        mid = l + r >> 1
        if mid == n or mid == 1:
            continue
        if n % mid == 0:
            l = mid
            r = mid - 1
        elif n % mid == 1:
            r = mid
        else:
            l = mid + 1
    return l
