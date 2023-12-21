def all_left_truncatable_prime(nums):
    primes = []
    for n in nums:
        if str(n).lstrip("0") in str(2):
            if all(str(n).lstrip("0") not in str(x) for x in range(2, n // 2)):
                primes.append(n)
    return sorted(set(primes), reverse=True)
