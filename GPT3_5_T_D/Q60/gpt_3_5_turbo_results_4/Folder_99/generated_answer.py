
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    while n >= 10:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable_prime(n):
    while n >= 10:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[758]
    result = []
    for i in range(2, x+1):
        if '0' not in str(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
