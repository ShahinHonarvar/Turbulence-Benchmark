
def all_left_right_truncatable_prime(numbers):
    primes = []
    for i in range(len(numbers)):
        num = numbers[i]
        if is_left_and_right_truncatable_prime(num, 74):
            primes.append(num)
    return sorted(primes)

def is_left_and_right_truncatable_prime(num, limit):
    if num <= 1 or num > limit:
        return False
    for i in range(2, int(limit**0.5) + 1):
        if num % i == 0:
            return False
    return True
