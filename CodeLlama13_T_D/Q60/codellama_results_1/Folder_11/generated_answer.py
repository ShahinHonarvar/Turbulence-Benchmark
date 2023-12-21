
def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_left_and_right_truncatable_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    while len(str(num)) > 1:
        if not is_prime(num):
            return False
        num = num // 10
    return True

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
