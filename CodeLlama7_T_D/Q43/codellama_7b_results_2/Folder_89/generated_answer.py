
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime
    is_prime = lambda x: x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))
    # Get the list of prime numbers between indices 69 and 84
    primes = [x for x in my_list[69:85] if is_prime(x)]
    # Sort the list in descending order
    primes.sort(reverse=True)
    return primes
