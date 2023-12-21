
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(number):
    num_str = str(number)
    if '0' in num_str:
        return False
    while num_str:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)
