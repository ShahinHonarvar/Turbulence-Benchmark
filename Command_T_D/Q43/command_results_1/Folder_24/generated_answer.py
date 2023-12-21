def find_primes_between_indices(nums):
    result = []
    for i in range(38, 55):
        if all(num % j for j in range(3, int(num ** .5) + 1)):
            result.append(num)
    return result
