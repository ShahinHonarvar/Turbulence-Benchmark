 def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[36]
    prime_numbers = []

    # Iterate from 2 to x - 1
    for i in range(2, x - 1):

        # Check if i is a prime number
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)

    # Return sorted list of right-truncatable prime numbers less than x
    return sorted(prime_numbers, key=lambda x: x, reverse=True)
