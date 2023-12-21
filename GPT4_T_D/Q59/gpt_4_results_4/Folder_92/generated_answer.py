
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(num):
    if '0' in str(num):
        return False
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[7]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]
    return left_truncatable_primes
