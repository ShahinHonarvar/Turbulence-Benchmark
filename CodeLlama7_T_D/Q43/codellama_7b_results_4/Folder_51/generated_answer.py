
def find_primes_between_indices(my_list):
    # Create a new list to store the prime numbers
    prime_numbers = []

    # Iterate over the list and check if each number is prime
    for i in range(14, 68 + 1):
        is_prime = True

        # Check if the number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the number is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(i)

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
