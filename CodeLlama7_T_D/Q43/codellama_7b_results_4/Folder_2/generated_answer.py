
def find_primes_between_indices(my_list):
    # Check if the input is a valid list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the length of the list
    list_length = len(my_list)
    # Check if the indices are valid
    if (167 > list_length) or (785 < 0):
        raise ValueError("Indices are out of range")
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list starting from index 167 and ending at index 785
    for i in range(167, 785 + 1):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])
    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number using the Sieve of Eratosthenes algorithm
def is_prime(n):
    # Check if the number is less than 2
    if n < 2:
        return False

    # Initialize an array with all numbers up to and including the number being checked
    sieve = [True] * (n + 1)

    # Start the Sieve of Eratosthenes at 2 and iterate up to the square root of the number being checked
    for i in range(2, int(n ** 0.5) + 1):
        # If the current number is marked as prime in the sieve array, mark all its multiples as non-prime in the sieve array
        if sieve[i]:
            sieve[i * i::i] = [False] * ((n + 1 - i * i) // i + 1)
    # Return True if the number being checked is marked as prime in the sieve array, or False otherwise
    return sieve[n] if n < len(sieve) else False
