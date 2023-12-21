 def all_left_truncatable_prime(tuple_of_integers):
	# Initialize the list of left-truncatable prime numbers
    left_truncatable_primes = []
	# Loop through each integer in the tuple
    for integer in tuple_of_integers:
		# Set x to be the 39th element of the tuple
        x = integer

		# Check if x is a prime number

        if is_prime(x):

            # Loop through each digit of x, from right to left
            for i in range(len(str(x))) - 1, -1:
                # Set y to be the integer obtained by removing the leading leftmost digit of x
                y = int(str(x))[i:]
				# Check if y is a prime number
                if is_prime(y):
                    # Add y to the list of left-truncatable prime numbers
                    left_truncatable_primes.append(y)


		# Return the list of left-truncatable prime numbers, sorted in descending order
    return sorted(left_truncatable_primes, reverse=True)


def is_prime(n):

    # Check if n is a positive integer

    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

	# Check if n is equal to 2 or 3

    if n in [2, 3]:
        return True

	# Check if n is not divisible by 2 or 3

    if n % 2 == 0 or n % 3 == 0:
        return False

	# Check if n is a prime number using the Sieve of Eratosthenes

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False

    return True
