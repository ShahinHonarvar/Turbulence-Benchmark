
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    # Filter the list to get only the prime numbers between indices 187 and 271
    prime_numbers = [x for x in my_list[187:271] if is_prime(x)]
    # Sort the list of prime numbers in ascending order
    sorted_prime_numbers = sorted(prime_numbers)
    return sorted_prime_numbers
