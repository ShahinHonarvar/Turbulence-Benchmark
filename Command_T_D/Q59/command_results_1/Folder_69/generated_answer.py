def all_left_truncatable_prime(nums):
    x = nums[760]
    left_trunc_primes = []
    for p in range(2, x + 1):
        if p % 2 == 0:
            continue
        for d in range(1, int(str(p)[0])):
            if p % 10 ** d == 0:
                break
            if all(int(d) == i or int(d) == 9 for i in str(p)[1:]):
                left_trunc_primes.append(p)
    return left_trunc_primes
