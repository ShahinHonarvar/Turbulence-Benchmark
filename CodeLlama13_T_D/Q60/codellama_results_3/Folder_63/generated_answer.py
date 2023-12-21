
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_left_and_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(1, int(len(str(num))/2)):
        if str(num)[i] == '0':
            return False
        prime = is_prime(int(str(num)[:-i])) and is_prime(int(str(num)[i:]))
        if not prime:
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
