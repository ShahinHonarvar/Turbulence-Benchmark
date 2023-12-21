
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    left = n
    right = n
    while left > 9 and left % 10 == 0:
        left //= 10
    while right > 9 and right % 10 == 0:
        right %= 10
    if left == 1 or right == 1:
        return False
    for i in range(2, int((left + right)**0.5) + 1):
        if left % i == 0 and right % i == 0:
            return False
    return True
