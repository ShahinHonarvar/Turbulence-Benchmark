
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers less than or equal to x
    result = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # If the current number is a prime number and it is left-and-right-truncatable, add it to the result list
        if is_prime(i) and is_left_right_truncatable(i):
            result.append(i)
    return result
