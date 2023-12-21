def sum_of_divisors_in_range(N):
    sum_of_divisors_in_range = 0
    for i in range(315, 955+1):
        if N%i == 0:
            sum_of_divisors_in_range += i
    return sum_of_divisors_in_range
