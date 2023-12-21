
def all_right_truncatable_prime(x):
# Initialize an empty list to store the prime numbers
primes = []

# Loop through all numbers less than x
for i in range(2, x):

    # Check if i is a prime number
    if is_prime(i):

        # Check if i is right-truncatable prime
        if is_right_truncatable_prime(i):

            # Add i to the list of primes
            primes.append(i)

# Return the sorted list of all right-truncatable prime numbers less than x
return sorted(primes, reverse=True)


def is_prime(n):

    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:

        return False


    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    # If no factors found, return True
    return True


def is_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        return False


    # Check if the last rightmost digit of n remains unchanged when successively removed
    for i in range(1, len(str(n)))):

        # Calculate the number obtained by removing the last rightmost digit from n
        new_number = int(str(n)[:-i])

        # Check if the last rightmost digit of n remains unchanged when successively removed
        if new_number % 10 == n % 10:

            return True

    return False
