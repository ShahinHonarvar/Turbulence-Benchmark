
def all_left_right_truncatable_prime(x):
    # Create an empty list to store the prime numbers
    prime_list = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number and it is left-and-right-truncatable prime
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_list.append(i)

    # Sort the list of prime numbers in ascending order
    prime_list.sort()

    return prime_list
