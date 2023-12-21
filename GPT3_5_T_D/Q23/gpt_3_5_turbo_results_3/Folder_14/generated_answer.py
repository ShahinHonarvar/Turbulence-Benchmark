
def find_divisors_in_range(num):
    divisors = []
    for divisor in range(1, num+1):
        if num % divisor == 0 and 6 <= divisor <= 8:
            divisors.append(divisor)
    return divisors
