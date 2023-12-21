
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all the elements in the list
    for i in range(35, 90):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(i ** 0.5) + 1):
            # If the current element is divisible by any number between 2 and the square root of the current element, it is not prime
            if i % j == 0:
                break

        # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime
        else:
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 35 to index 89, both inclusive
    return sorted(prime_numbers, reverse=True)
