
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Iterate through the range of integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current integer to the list of prime numbers
                prime_list.append(i)
    return prime_list
