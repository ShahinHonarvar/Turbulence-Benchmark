
def find_primes_between_indices(my_list):
    # Define a list to store the prime numbers
    prime_numbers = []

    # Loop through the list and check if each element is prime
    for i in range(596, 934 + 1):
        # Check if the number is divisible by any number between 2 and the square root of the number
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the number is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(i)

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
