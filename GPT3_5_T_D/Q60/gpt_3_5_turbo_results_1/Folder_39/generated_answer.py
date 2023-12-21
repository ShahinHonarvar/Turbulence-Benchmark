
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    num_str = str(n)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:i+1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    truncatable_primes = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
