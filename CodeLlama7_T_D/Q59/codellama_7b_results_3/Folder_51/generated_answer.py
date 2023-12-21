 def all_left_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[54]
    prime_numbers = []
    for i in range(2, x):
        # Check if the number is a prime number
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the number is a prime number and it is left-truncatable prime number
        if is_prime and not str(i).startswith("0"):
            prime_numbers.append(i)
    return sorted(prime_numbers)
