def find_divisors_in_range(n):
    if n < 39 or n > 57:
        return []
    divisor_list = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            if i not in divisor_list:
                divisor_list.append(i)
            if n // i not in divisor_list:
                divisor_list.append(n // i)
    return sorted(divisor_list)
