
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[:i])) or not is_prime(int(n_str[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    truncatable_primes = []
    for num in range(2, x+1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
