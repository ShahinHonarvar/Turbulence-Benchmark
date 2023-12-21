
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[79]
    primes = []
    for n in range(x - 1, 0, -1):
        if '0' not in str(n):
            truncatable = True
            while truncatable and n > 0:
                if not is_prime(n):
                    truncatable = False
                n //= 10
            if truncatable:
                primes.append(n)
    return sorted(primes, reverse=True)
