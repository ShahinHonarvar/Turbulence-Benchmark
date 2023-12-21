
def find_primes_between_indices(my_list):
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Iterate through the list of integers starting from index 271
    for i in range(271, len(my_list)):
        # Check if the current number is prime by iterating from 2 to the square root of the number
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the current number is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 271 to index 737, both inclusive
    return sorted(prime_numbers)
