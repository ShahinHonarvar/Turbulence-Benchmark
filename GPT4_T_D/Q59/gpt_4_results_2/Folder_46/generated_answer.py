
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def truncate_prime(num):
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[33]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i) and truncate_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
