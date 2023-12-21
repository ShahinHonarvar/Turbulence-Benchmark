
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list of integers
    for i in range(112, 361 + 1):
        # Check if the number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If the number is divisible, break out of the loop
                break

        else:

            # If the number is not divisible by any number between 2 and the square root of the number, it is prime
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)
