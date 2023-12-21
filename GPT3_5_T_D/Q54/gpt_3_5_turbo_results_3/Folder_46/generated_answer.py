
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[33]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncated = str(i)[:-1]
            while truncated:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[:-1]
            else:
                primes.append(i)
    return sorted(primes)
