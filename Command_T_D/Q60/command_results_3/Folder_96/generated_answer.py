
def all_left_right_truncatable_prime(nums):
    primes = []
    for i in range(2, max(nums) + 1):
        if all(str(i).rstrip("0")[::-1].count(d) == 1 for d in str(i)[::-1]):
            primes.append(i)
    return primes
