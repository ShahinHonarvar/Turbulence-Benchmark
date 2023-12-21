
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 61 to index 79, both inclusive
    for i in range(61, 80):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If the current element is divisible by any number between 2 and the square root of the current element, it is not prime
                break

        else:

            # If the loop completes without breaking, the current element is prime
            prime_numbers.append(i)

    return sorted(prime_numbers)
