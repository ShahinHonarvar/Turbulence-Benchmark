
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_left_and_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(1, int(len(str(num))/2)+1):
        left = int(str(num)[:i])
        right = int(str(num)[-i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
