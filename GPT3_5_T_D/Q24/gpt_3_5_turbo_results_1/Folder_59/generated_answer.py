
def sum_of_divisors_in_range(num):
    divisors = []
    for divisor in range(1, num + 1):
        if num % divisor == 0 and 3 <= divisor <= 5:
            divisors.append(divisor)
    return sum(divisors)
