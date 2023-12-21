
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        truncated = str(num)
        while truncated != '':
            if not is_prime(int(truncated)):
                truncatable = False
                break
            truncated = truncated[1:]
        if truncatable:
            primes.append(num)
    return sorted(primes)
