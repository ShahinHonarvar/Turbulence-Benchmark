
def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for num in range(1, n+1):
        if n % num == 0 and 14 <= num <= 48:
            divisors_sum += num
    return divisors_sum
