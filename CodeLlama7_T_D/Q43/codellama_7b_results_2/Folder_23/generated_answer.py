
def find_primes_between_indices(my_list):
    # Find all prime numbers in the specified range
    primes = []
    for i in range(20, 48+1):
        if is_prime(i):
            primes.append(i)
    # Sort the list of prime numbers in descending order
    primes.sort(reverse=True)
    return primes
