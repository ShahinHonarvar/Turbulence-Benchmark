
def all_left_truncatable_prime(nums):
    result = []
    for n in nums:
        if str(n).startswith('0'):
            continue
        if is_left_truncatable_prime(n):
            result.append(n)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(1, int(len(str(n)) / 2)):
        if not is_prime(n - i * 10 ** i):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
