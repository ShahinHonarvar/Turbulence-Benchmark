
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda n: (n > 1) and all(n % i for i in range(2, int(n ** 0.5) + 1))
    # Return the sorted list of all prime numbers from index 69 to index 80, both inclusive
    return sorted([my_list[i] for i in range(69, 81) if is_prime(my_list[i])], reverse=False)]
