
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list, reverse=True)

# Check if a number is prime using the Sieve of Eratosthenes
def is_prime(n):

    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # If the number is divisible by 2 to n-1, it is not prime
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is divisible only by 1 and itself, it is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # If the number is not a prime number, it is not left-and-right-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number contains 0
    for i in str(n):
        if i == "0":
            return False

    # Check if the number remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[:i] + str(n)[i+1:]))):
            return False

    # If the number passes all the checks, it is left-and-right-truncatable prime number
    return True
