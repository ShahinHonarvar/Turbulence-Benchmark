
def all_right_truncatable_prime(nums):
    x = nums[43]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            if j == 0:
                primes.append(i)
    return sorted(primes)
