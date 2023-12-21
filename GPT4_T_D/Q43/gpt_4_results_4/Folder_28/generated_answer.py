
def find_primes_between_indices(lst):
    subset = lst[38:55]
    primes = [num for num in subset if all(num%i != 0 for i in range(2, int(num**0.5)+1)) and num > 1]
    return sorted(primes, reverse=True)
