
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for n in numbers:
        if is_left_and_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(1, int(len(str(n))/2)):
        if str(n)[i] == '0':
            return False
        if not is_prime(int(str(n)[:-i])) or not is_prime(int(str(n)[i+1:])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
