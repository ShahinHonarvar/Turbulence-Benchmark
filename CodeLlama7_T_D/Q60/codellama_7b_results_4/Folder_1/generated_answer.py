
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the range of prime numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Initialize a string variable to store the representation of i
            str_rep = str(i)

            # Check if i contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
            if (not "0" in str_rep) and (is_prime(int(str_rep[1:])) or is_prime(int(str_rep[:-1])))):
                # If the above condition is met, add i to the results list
                results.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(results, reverse=True)

# Check if a number is a prime number using the Sieve of Eratosthenes algorithm
def is_prime(n):
    # Initialize a boolean variable to store the result of the primality check
    is_prime = True

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by an integer between 2 and the square root of n, it is not prime
        if n % i == 0:
            is_prime = False
            break

    # Return the result of the primality check
    return is_prime
