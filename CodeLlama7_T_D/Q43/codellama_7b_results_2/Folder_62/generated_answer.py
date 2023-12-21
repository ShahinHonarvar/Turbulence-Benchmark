
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list from index 29 to index 97
    for i in range(29, 100):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            # If the current number is divisible by any number between 2 and the square root of the current number, it is not prime
            if i % j == 0:
                break

        # If the current number is not divisible by any number between 2 and the square root of the current number, it is prime
        else:
            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers
