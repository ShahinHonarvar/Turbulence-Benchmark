
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the right-truncatable prime numbers
    right_truncatable_primes = []
    # Loop through each element in the tuple
    for i in range(len(tuple)):
        # Check if the current element is a prime number
        if is_prime(tuple[i]):
            # Initialize a variable to store the right-truncatable prime number
            right_truncatable_prime = tuple[i]
            # Loop through each digit in the rightmost part of the prime number
            for j in range(len(str(right_truncatable_prime)) - 1, -1, -1)):
                # Check if the current digit is not equal to zero
                if str(right_truncatable_prime)[j] != "0":
                    # Remove the last rightmost digit of the prime number
                    right_truncatable_prime = int(str(right_truncatable_prime)[:j])
                    # Check if the removed digit is still a prime number
                    if is_prime(right_truncatable_prime):
                        # Add the right-truncatable prime number to the list of all right-truncatable prime numbers less than x
                        right_truncatable_primes.append(right_truncatable_prime)
    # Sort the list of all right-truncatable prime numbers in ascending order
    right_truncatable_primes = sorted(right_truncatable_primes)
    return right_truncatable_primes
