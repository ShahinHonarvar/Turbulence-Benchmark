
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate through the tuple and check if each element is a prime number
    for i in tuple:
        if is_prime(i) == True:
            # If the element is a prime number, add it to the list
            prime_list.append(i)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_list, reverse=True)

# Define a function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is a multiple of 2 to 10
        for i in range(2, 11):
            if n % i == 0:
                # If it is a multiple, return False
                return False

        # If it is not a multiple of 2 to 10, return True
        return True

    # If n is less than or equal to 1, return False
    else:
        return False
