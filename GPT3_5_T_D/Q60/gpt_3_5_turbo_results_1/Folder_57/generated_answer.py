
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n))):
        left_num = int(str(n)[i:])
        right_num = int(str(n)[:-i])
        if not is_prime(left_num) or not is_prime(right_num):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_primes = []
    for i in range(x, 9, -1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
