
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 830 to index 849
    for i in range(830, 850):

        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime
        else:
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 830 to index 849, both inclusive
    return sorted(prime_numbers)
