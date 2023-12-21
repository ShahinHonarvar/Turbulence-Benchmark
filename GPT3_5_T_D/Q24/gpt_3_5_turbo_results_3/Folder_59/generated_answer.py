
def sum_of_divisors_in_range(number):
    divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0 and 3 <= divisor <= 5:
            divisors.append(divisor)
    return sum(divisors) if divisors else 0
