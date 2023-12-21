def find_primes_between_indices(list):
    return sorted(list[43:59] for index in range(43, 59 + 1) if all(x % index != 0 and x % index != 1 for x in range(2, index // 2)))
