
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i can be divided by 2 without leaving a remainder
            if i % 2 == 0:

                # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
                if is_prime(i // 10) or is_prime(i // 100):
                    prime_list.append(i)

            # Check if i can be divided by 3 without leaving a remainder
            if i % 3 == 0:

                # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
                if is_prime(i // 10) or is_prime(i // 100):
                    prime_list.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_list)

# Define a function to check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n without leaving a remainder
            if n % i == 0:
                return False

    # If the number is greater than 1 and does not have any factors other than 1 and itself, it is prime
    return True
