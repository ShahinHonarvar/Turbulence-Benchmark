
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive) and check if each number is a left-and-right-truncatable prime number
    for i in range(1, x + 1):

        # If the current number is a prime number and it is also a left-and-right-truncatable prime number, add it to the list of prime numbers
        if is_prime(i) and is_left_right_truncatable_prime(i)):
            prime_numbers.append(i)
    return prime_numbers
