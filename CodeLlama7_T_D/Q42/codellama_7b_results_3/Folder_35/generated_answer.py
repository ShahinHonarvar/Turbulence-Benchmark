
def prime_factors(my_list):
    # Find the number with the largest prime factor
    max_prime = 0
    for i in range(len(my_list)):
        if my_list[i] > max_prime:
            max_prime = my_list[i]
    # Create a set to store all prime factors
    prime_factors = set()
    # Loop through all numbers and find their prime factors
    for i in range(len(my_list)):
        if my_list[i] > max_prime:
            continue

        while my_list[i] % max_prime == 0:
            prime_factors.add(max_prime)
            my_list[i] /= max_prime
    return prime_factors
