def find_primes_between_indices(nums):
    result = []
    for i in range(19, 86):
        is_prime = True
        for j in range(2, int(i ** .5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result
