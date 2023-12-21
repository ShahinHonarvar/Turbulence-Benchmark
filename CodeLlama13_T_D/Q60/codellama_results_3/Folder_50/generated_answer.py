
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_right_truncatable_prime(num):
    if str(num).count('0') > 0:
        return False
    for i in range(len(str(num))-1, 1, -1):
        if not is_prime(int(str(num)[:i])) or not is_prime(int(str(num)[i+1:])):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
