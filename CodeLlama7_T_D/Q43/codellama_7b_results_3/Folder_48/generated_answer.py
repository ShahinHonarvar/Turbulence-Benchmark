
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime
    is_prime = lambda x: x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))
    # Find the indices of the prime numbers in the list
    prime_indices = [i for i, x in enumerate(my_list) if is_prime(x)]
    # Extract the prime numbers from the list using the indices
    primes = [my_list[i] for i in prime_indices]
    # Sort the prime numbers in ascending order
    primes.sort()
    return primes
