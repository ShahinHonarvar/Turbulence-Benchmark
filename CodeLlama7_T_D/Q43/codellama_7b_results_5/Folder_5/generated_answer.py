
def find_primes_between_indices(my_list):
    # Initialize variables for indices and prime numbers
    start_index = 46
    end_index = 75
    prime_numbers = []
    
    # Loop through the list starting from the specified index
    for i in range(start_index, len(my_list)):
        # Check if the current number is a prime number
        if is_prime(my_list[i]):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(my_list[i])
    
    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number by dividing it by all the numbers less than or equal to its square root
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
