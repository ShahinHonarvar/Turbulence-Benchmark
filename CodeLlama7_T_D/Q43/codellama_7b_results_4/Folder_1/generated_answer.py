
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers from index 87 to index 89, both inclusive
    for i in range(87, 90):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            if my_list[i] % j == 0:
                # If the current element is divisible by any number between 2 and the square root of the current element, it is not a prime number
                break

        else:

            # If the loop completes without breaking, the current element is a prime number

            prime_numbers.append(my_list[i])

    return sorted(prime_numbers)
