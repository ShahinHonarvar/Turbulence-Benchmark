def all_left_truncatable_prime(nums):
    primes = [x for x in range(2, nums[94]) if all(str(x).count(d) == 1 for d in str(x) if d == '0' or d == '1' or d == '2' or d == '3' or d == '5' or d == '6' or d == '7' or d == '8' or d == '9')]
    return sorted(primes)
