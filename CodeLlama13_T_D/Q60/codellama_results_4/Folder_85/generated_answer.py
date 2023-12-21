
def all_left_right_truncatable_prime(nums):
    x = nums[94]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') or str(i).endswith('0')):
            primes.append(i)
    return sorted(primes)
