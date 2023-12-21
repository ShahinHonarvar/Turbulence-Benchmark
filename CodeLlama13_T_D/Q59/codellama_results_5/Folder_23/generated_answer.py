
def all_left_truncatable_prime(nums):
    x = nums[77]
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and not any(str(i).startswith('0') for i in range(2, int(str(i)[1:]))) and all(is_prime(int(str(i)[j:])) for j in range(len(str(i)))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
