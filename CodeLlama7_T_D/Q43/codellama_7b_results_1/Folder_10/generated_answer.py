
def find_primes_between_indices(my_list):
    # Create a new list to store the prime numbers
    prime_numbers = []

    # Iterate over the list of integers, starting from index 30
    for i in range(30, len(my_list)):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in ascending order
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:
                # If it is divisible, it is not a prime number
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number, it is a prime number
    return True
