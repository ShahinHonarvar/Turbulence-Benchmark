def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    if len(divisors) > 0:
        divisors.sort()
        return sum(divisors[3:6])
    else:
        return 0
