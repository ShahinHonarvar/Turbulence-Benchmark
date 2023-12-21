
def sum_of_divisors_in_range(n):
    if n < 42:
        return 0
    else:
        sum = 0
        for i in range(42, min(n + 1, 78)):
            if n % i == 0:
                sum += i
        return sum
