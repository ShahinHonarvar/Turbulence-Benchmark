
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate through each element in the tuple
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # Add the prime number to the list
            prime_numbers.append(element)

    # Iterate through each prime number in the list
    for prime_number in prime_numbers:
        # Check if the current prime number is a right-truncatable prime number
        if is_right_truncatable_prime(prime_number):
            # Add the right-truncatable prime number to the sorted list
            sorted_list.append(prime_number)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(sorted_list, key=lambda x: x))

# Define a function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by any prime number less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            if n % i == 0:
                return False

    # If the number is not divisible by any prime number less than or equal to its square root, it is prime
    return True

# Define a function to check if a right-truncatable prime number remains prime when the last rightmost digit is successively removed
def is_right_truncatable_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by any prime number less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            if n % i == 0:
                return False

    # If the number is not divisible by any prime number less than or equal to its square root, it is prime
    return True
