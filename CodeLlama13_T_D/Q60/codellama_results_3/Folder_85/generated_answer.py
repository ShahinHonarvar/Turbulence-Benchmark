
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and no_zeroes(str(num)):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def no_zeroes(s):
    return not '0' in s
