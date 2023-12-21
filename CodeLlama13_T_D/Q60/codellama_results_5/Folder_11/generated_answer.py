
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_left_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(1, int(len(str(num))/2)):
        if str(num)[i] == '0':
            return False
        if not is_prime(num) and not is_prime(int(str(num)[:-i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
