
def all_right_truncatable_prime(nums):
    right_truncatable_primes = []
    for num in nums:
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num > 10:
        last_digit = num % 10
        num //= 10
        if not is_prime(num * 10 + last_digit):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
