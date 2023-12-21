def find_primes_between_indices(nums):
    result = []
    for i in range(76, 92+1):
        if all(num % j for j in range(2, int(num**(0.5))+1)):
            result.append(i)
    return result
