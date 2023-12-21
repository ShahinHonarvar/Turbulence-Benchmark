
def prime_factors(numbers):
    result = set()
    for number in numbers:
        if is_prime(number):
            result.add(number)
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
