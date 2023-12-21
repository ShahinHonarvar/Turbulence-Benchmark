
def sum_of_divisors_in_range(n):
    if n < 224 or n > 584:
        return 0
    else:
        sum = 0
        for i in range(224, 585):
            if n % i == 0:
                sum += i
        return sum
