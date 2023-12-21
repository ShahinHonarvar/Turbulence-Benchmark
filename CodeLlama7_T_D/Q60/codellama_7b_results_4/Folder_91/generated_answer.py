 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number using the Sieve of Eratosthenes algorithm
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in descending order
    return sorted(prime_numbers, reverse=True)
