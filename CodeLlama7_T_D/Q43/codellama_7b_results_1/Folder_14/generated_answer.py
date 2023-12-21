
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list and check if each number is prime
    for i in range(26, len(my_list)):
        if is_prime(my_list[i]):
            # If the number is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 26 to index 30, both inclusive
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime by iterating from 2 to the square root of the number and checking if it divides without a remainder
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
