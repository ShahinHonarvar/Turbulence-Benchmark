
def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:i+1])) or not is_prime(int(str_n[i+1:])):
            return False
    return True
