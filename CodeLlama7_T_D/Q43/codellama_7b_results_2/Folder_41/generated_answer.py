 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list starting from index 45
    for i in range(45, len(my_list)):
        # Check if the current number is prime
        if is_prime(my_list[i]):
            # If it is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 45 to index 80, both inclusive
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n-1, it is prime
    return True
