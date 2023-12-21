
def all_right_truncatable_prime(nums):
    x = nums[74]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    right_truncatable_prime_numbers = []
    for p in prime_numbers:
        if is_right_truncatable_prime(p):
            right_truncatable_prime_numbers.append(p)
    return sorted(right_truncatable_prime_numbers)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(p):
    while p > 0:
        if not is_prime(p):
            return False
        p //= 10
    return True
