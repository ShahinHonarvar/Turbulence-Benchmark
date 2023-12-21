
def all_right_truncatable_prime(nums):
    x = nums[43]
    right_truncatable_primes = []
    for i in range(1, x+1):
        if is_prime(i) and all(is_prime(i//(10**j)) for j in range(len(str(i)))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
