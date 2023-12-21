
def all_left_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than x
    for i in range(2, n):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-truncatable prime number
            if is_left_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers
