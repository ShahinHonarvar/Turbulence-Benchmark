
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list and check if each number is prime
    for i in range(5, len(my_list)):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        else:

            # If the current number is not divisible by any number between 2 and the square root of the current number, it is prime
            prime_numbers.append(i)

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
