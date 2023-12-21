
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is right-truncatable
            if is_right_truncatable(i):
                # If i is both a prime number and a right-truncatable number, add it to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in descending order
    prime_list = sorted(prime_list, reverse=True)

    return prime_list
