def sum_of_divisors_in_range(x):
    divisor_sum = 0
    for i in range(x // 2, 0, -1):
        if i * i <= x:
            for j in range(x // i, 0, -1):
                if j * j <= x:
                    divisor_sum += i * j
    return max(divisor_sum, 0)
