
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and has_no_zeroes(num) and is_left_and_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_no_zeroes(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def is_left_and_right_truncatable(n):
    left, right = str(n), str(n)
    while len(left) > 1 or len(right) > 1:
        if not is_prime(int(left)):
            return False
        if not is_prime(int(right)):
            return False
        left, right = left[1:], right[:-1]
    return True
