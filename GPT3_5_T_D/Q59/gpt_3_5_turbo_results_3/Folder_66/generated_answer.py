
def all_left_truncatable_prime(numbers):
    primes = []
    for num in range(numbers[25]-1, 0, -1):
        if num == 1:
            continue
        if is_left_truncatable_prime(num):
            primes.append(num)
    return primes

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num == 1:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    num_str = str(num)
    while num_str:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True
