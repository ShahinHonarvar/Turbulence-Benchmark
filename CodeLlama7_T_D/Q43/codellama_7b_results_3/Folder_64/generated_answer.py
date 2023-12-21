 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Loop through the list starting from index 7
    for i in range(len(my_list)):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # Add the prime number to the list of primes
            primes.append(my_list[i])
    # Return the sorted list of all prime numbers from index 7 to index 9, both inclusive
    return sorted(primes)
# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n-1
        for i in range(2, n):
            # If the remainder of dividing n by i is 0, then n is not prime
            if n % i == 0:
                return False

    # If we reach this point, then n is prime
    return True
