
def all_left_right_truncatable_prime(nums):
    # your code here
    primes = []
    for n in nums:
        if is_left_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)[::-1] if primes else []

def is_left_right_truncatable_prime(n):
    # your code here
    return all(int(d) > 0 for d in str(n)) and str(n) in range(str(2), str(n + 1))
