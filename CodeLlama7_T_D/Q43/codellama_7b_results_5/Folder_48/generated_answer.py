
def find_primes_between_indices(my_list):
    # Create a list to store the prime numbers
    prime_numbers = []

    # Loop through the list and check if each number is prime
    for i in range(274, 650):
        # Check if the current number is divisible by any other number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        else:

            # If the loop completes without breaking, the current number is prime
            prime_numbers.append(i)

    return sorted(prime_numbers)
