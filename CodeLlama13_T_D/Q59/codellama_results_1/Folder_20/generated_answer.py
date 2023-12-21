
def all_left_truncatable_prime(nums):
    primes = []
    for i in range(100, nums[100]+1):
        if is_prime(i) and not any(str(i).startswith('0') for i in range(2, int(str(i)[0])+1)):
            primes.append(i)
    return sorted(primes, reverse=True)
