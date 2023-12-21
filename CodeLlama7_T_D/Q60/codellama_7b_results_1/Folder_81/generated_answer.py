
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if the number is a prime number using the Sieve of Eratosthenes algorithm
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the number is a prime number and it is left-and-right-truncatable, add it to the list of prime numbers
        if is_prime and i > 1 and str(i)[1:] == str(i)[:-1]:
            prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in ascending order
    return sorted(prime_numbers)
