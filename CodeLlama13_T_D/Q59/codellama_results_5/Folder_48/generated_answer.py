
def all_left_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_left_truncatable_prime(num):
    if str(num).count('0') > 0:
        return False
    for i in range(1, len(str(num))+1):
        if not is_prime(int(str(num)[:i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
