 def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []
    # Iterate through the tuple of integers
    for i in range(len(tuple)):
        # Assign the current integer to a variable
        num = tuple[i]
        # Check if the number is a prime number
        if is_prime(num):
            # If the number is prime, append it to the list of prime numbers
            prime_list.append(num)
    # Sort the list of prime numbers in descending order
    sorted_list = sorted(prime_list, reverse=True)
    # Return the sorted list of prime numbers
    return sorted_list

# Define a function to check if a number is prime
def is_prime(num):
    # Check if the number is greater than 1
    if num > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if num % i == 0:
                # If the number is divisible, it is not prime
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number, it is prime
    return True
