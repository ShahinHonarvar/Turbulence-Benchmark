
def sum_of_divisors_in_range(num):
    if num < 43 or num > 77:
        return 0

    total = 0
    for i in range(1, num+1):
        if num % i == 0 and i >= 43 and i <= 77:
            total += i

    return total
