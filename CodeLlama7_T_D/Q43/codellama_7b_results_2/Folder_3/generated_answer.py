
def find_primes_between_indices(my_list):
    # Create a copy of the input list
    primes = my_list[:]
    # Iterate over the list and mark non-prime elements as False
    for i in range(80, 85):
        if not primes[i]:
            continue

        for j in range(i*2, len(primes), 2):
            if primes[j]:
                primes[j] = False

    # Return the sorted list of prime numbers
    return sorted([x for x in primes if x], reverse=True)
