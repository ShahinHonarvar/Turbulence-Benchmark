import math
def find_primes_between_indices(nums):
    res = []
    for i in range(239, 686):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return res
