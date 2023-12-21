
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through each element in the tuple
    for i in range(len(tuple)):

        # Get the current element from the tuple
        current_element = tuple[i]

        # Check if the current element is a prime number
        if is_prime(current_element):

            # If it is, add it to the list of prime numbers
            prime_list.append(current_element)

    # Loop through each prime number in the list
    for i in range(len(prime_list)):

        # Get the current prime number from the list
        current_prime = prime_list[i]

        # Check if the current prime number is right-truncatable
        if is_right_truncatable(current_prime):

            # If it is, add it to the final list of prime numbers
            final_prime_list.append(current_prime)

    # Sort the final list of prime numbers in descending order
    final_prime_list.sort(reverse=True)

    # Return the sorted final list of prime numbers
    return final_prime_list

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if n is an integer greater than 1
    if n > 1:

        # Loop through all the numbers from 2 to n-1
        for i in range(2, n):

            # If any of the numbers divide n, it is not prime
            if n % i == 0:
                return False

    # If none of the numbers from 2 to n-1 divide n, it is prime
    return True

# Define a function to check if a number is right-truncatable
def is_right_truncatable(n):

    # Check if n is an integer greater than 1
    if n > 1:

        # Loop through all the numbers from 2 to n-1
        for i in range(2, n):

            # If any of the numbers divide n, it is not right-truncatable
            if n % i == 0:
                return False

    # If none of the numbers from 2 to n-1 divide n, it is right-truncatable
    return True
