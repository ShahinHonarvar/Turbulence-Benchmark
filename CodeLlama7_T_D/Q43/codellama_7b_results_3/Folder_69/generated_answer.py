
def find_primes_between_indices(my_list):
    # Create a new list to store the prime numbers
    prime_numbers = []

    # Iterate through the list of integers
    for i in range(497, 930 + 1):
        # Check if the number is prime
        if is_prime(my_list[i]):
            # If it is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime by iterating from 2 to the square root of the number
def is_prime(n):
    # If the number is less than or equal to 1, it is not prime
    if n <= 1:
        return False

    # If the number is divisible by 2 to the square root of the number, it is not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If none of the above conditions are met, the number is prime
    return True
