 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
        if not is_prime(int(str_n[:i+1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
