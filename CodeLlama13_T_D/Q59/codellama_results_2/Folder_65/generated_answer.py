
def all_left_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') for _ in range(len(str(i)))):
            primes.append(i)
    return sorted(primes)
