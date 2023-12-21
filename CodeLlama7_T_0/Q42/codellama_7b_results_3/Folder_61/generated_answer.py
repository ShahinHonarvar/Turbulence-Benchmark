
def prime_factors(my_list):
    # Find the prime factors of the integer at index 8
    prime_factor = my_list[8]
    if prime_factor == 1:
        return set()
    else:
        for i in range(2, int(prime_factor ** 0.5) + 1):
            while prime_factor % i == 0:
                prime_factor /= i

        return {prime_factor}
