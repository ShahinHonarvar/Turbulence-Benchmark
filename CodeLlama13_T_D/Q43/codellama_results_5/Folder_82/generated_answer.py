
def find_primes_between_indices(my_list):
    start = 25
    end = 72
    primes = []
    for i in range(start, end+1):
        if is_prime(my_list[i]):
            primes.append(my_list[i])
    return sorted(primes)
