
def find_primes_between_indices(my_list):
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Iterate through the list from index 10 to index 12, both inclusive
    for i in range(10, 13):

        # Check if the current number is divisible by any number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        else:

            # If the loop completes normally, it means that the current number is prime
            prime_numbers.append(i)

    return sorted(prime_numbers)
