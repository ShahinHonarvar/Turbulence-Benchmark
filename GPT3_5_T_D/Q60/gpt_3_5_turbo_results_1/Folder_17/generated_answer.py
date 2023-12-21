
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    n_str = str(n)
    digits = len(n_str)
    for i in range(digits):
        if n_str[i] == '0':
            return False
        if not is_prime(int(n_str[:digits-i])) or not is_prime(int(n_str[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_left_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
