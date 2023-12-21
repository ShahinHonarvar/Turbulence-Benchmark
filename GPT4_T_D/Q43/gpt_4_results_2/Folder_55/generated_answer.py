
def find_primes_between_indices(lst):
    is_prime = lambda num: num > 1 and all(num%i != 0 for i in range(2, int(num**0.5) + 1))
    prime_nums = [num for num in lst[2:3] if is_prime(num)]
    return sorted(prime_nums)
