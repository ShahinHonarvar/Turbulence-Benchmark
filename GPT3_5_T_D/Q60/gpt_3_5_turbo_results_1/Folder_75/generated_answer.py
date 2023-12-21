
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(nums):
    x = nums[41]
    primes = []
    
    def is_truncatable_prime(num):
        if len(str(num)) < 3:
            return is_prime(num)
        if not is_prime(num):
            return False
        if not is_truncatable_prime(int(str(num)[1:])):
            return False
        return is_truncatable_prime(int(str(num)[:-1]))
    
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            primes.append(num)
    
    return primes
