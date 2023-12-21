
def all_left_truncatable_prime(tuple_of_ints):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for integer in tuple_of_ints:

        # Check if the integer is a prime number
        if is_prime(integer):

            # If it is, add it to the list of prime numbers
            prime_numbers.append(integer)

# Define a function to check if an integer is a prime number
def is_prime(n):

    # Check if n is less than 2
    if n < 2:

        return False


    # Check if n is divisible by 2 to n-1
    for i in range(2, n):

        if n % i == 0:

            return False


    # If none of the above conditions are true, it must be a prime number
    return True
