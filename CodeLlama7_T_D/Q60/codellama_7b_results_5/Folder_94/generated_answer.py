
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_list = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    left_right_prime_list = []
    # Iterate over the prime numbers in the list and check if they are left-and-right-truncatable prime numbers
    for prime in prime_list:
        # Check if the leading leftmost digit is equal to 1

        if str(prime)[0] == '1':
            # If it is, check if it remains a prime number when the last rightmost digit is simultaneously removed down to a one- or two-digit prime.
            if all(prime % i != 0 for i in range(2, int(str(prime)[1:]) ** 0.5) + 1)):
                # If it does, add the left-and-right-truncatable prime number to the list.
                left_right_prime_list.append(prime)
    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x.
    return sorted(left_right_prime_list)
