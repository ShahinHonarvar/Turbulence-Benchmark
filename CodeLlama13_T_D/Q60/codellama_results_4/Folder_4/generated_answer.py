
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and not any(str(num).count(i) > 1 for i in '0123456789'):
            primes.append(num)
    return sorted(primes, reverse=True)
