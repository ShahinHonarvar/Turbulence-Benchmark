
def all_left_truncatable_prime(nums):
    x = nums[42]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not any('0' in str(i)[:j] for j in range(1, len(str(i))+1)):
            primes.append(i)
    return sorted(primes)
