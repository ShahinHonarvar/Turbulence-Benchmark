def find_divisors_in_range(n):
    if n < 4 or n > 9:
        return []
    divisor_list = []
    for i in range(1, n // 2):
        if n % i == 0:
            if i in range(4, 9):
                divisor_list.append(i)
            if i * i != n:
                divisor_list.append(n // i)
    return sorted(divisor_list)
