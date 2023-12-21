def all_left_truncatable_prime(nums):
    return sorted(nums for num in nums if all(int(d) for d in str(num) if d!='0' and all(isprime(int(d)) for d in str(num) if d!=d)))
