
def all_left_truncatable_prime(nums):
    left_trunc_primes = []
    for num in nums:
        if str(num).count('0') == 0 and is_prime(num) and all(is_prime(int(str(num)[1:i])) for i in range(len(str(num)), 0, -1)):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes)
