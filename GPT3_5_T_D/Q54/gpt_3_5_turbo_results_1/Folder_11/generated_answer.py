
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[86]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            n = num
            while n > 0:
                if not is_prime(n):
                    truncatable = False
                    break
                n //= 10
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
