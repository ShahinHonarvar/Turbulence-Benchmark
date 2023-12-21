
def find_primes_between_indices(my_list):
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Loop through the list of integers
    for i in range(17, 40):
        # Check if the number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        # If the number is prime, add it to the list
        else:
            prime_numbers.append(i)

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
