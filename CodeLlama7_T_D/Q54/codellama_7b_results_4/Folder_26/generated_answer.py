
def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 2 to n
    for i in range(2, n + 1):

        # Check if i is a prime number
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If i is a right-truncatable prime number, add it to the list
        if is_prime:
            prime_list.append(i)

    # Sort the list in descending order and return it
    return sorted(prime_list, reverse=True)
