
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)
    # Filter the list to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = []
    for i in prime_numbers:
        is_left_right_truncatable_prime = True
        for j in range(1, int(i ** 0.5) + 1):
            if str(i)[-j:] == "0":
                is_left_right_truncatable_prime = False
                break

        if is_left_right_truncatable_prime:
            left_right_truncatable_prime_numbers.append(i)
    # Sort the list in ascending order and return it
    left_right_truncatable_prime_numbers.sort()
    return left_right_truncatable_prime_numbers
