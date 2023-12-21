
def find_primes_between_indices(my_list):
    # Initialize a new list to store the prime numbers
    prime_numbers = []

    # Loop through the list and check if each element is prime
    for i in range(459, 782):
        # Check if the number is divisible by any other number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        else:

            # If the number is not divisible by any other number between 2 and the square root of the number, it is prime
            prime_numbers.append(i)

    return sorted(prime_numbers)
