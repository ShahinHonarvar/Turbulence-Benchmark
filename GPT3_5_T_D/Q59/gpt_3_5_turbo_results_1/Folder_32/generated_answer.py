
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[42]
    primes = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            truncated = str(i)
            while truncated:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[1:]
            else:
                primes.append(i)
    return sorted(primes)
