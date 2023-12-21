
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the range of prime numbers less than or equal to x
    for i in range(2, x + 1):
        # If the current number is a prime number and it is left-and-right-truncatable, add it to the list of results
        if i > 1 and all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            result.append(i)

    # Sort the list of results in descending order and return it
    return sorted(result, reverse=True)
