
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers, starting from index 1 and ending at index 5, both inclusive
    for i in range(1, len(my_list)):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(i ** 0.5) + 1):
            # If the current element is divisible by any number between 2 and the square root of the current element, it is not prime
            if i % j == 0:
                break

        # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime
        else:
            prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers
