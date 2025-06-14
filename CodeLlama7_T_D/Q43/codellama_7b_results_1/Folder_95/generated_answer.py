
def find_primes_between_indices(my_list):
    # Define a function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    # Define a list to store the prime numbers
    prime_numbers = []

    # Iterate through the list of integers and check for prime numbers
    for i in range(75, 86):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)
