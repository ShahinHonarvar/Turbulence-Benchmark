
def all_left_right_truncatable_prime(nums):
    return sorted(nums for num in nums if is_left_right_truncatable_prime(num))

def is_left_right_truncatable_prime(num):
    for i in range(num, 1, -1):
        if is_prime(i):
            return True
    return False

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    maxDivisor = num**0.5
    if maxDivisor < 6:
        return True
    for i in range(5, maxDivisor + 1):
        if num % i == 0:
            return False
    return True
