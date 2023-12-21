def find_primes_between_indices(nums):
    result = []
    for i in range(55, 77):
        if is_prime(i):
            result.append(i)
    return result
def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    maxDivisor = num**(0.5)
    if maxDivisor * maxDivisor <= num:
        return False
    return all(num % d for d in range(5, maxDivisor, 6))
