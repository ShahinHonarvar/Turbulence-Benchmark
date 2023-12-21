
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 1 to x - 1
    for i in range(1, x):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the leading leftmost digit of i is successively removed, then all resulting numbers are prime
            if all(is_prime(i // 10**j) for j in range(len(str(i)))):

                # Add i to the list of results
                result.append(i)

    # Return the sorted list of results
    return sorted(result, reverse=True)

# Check if a number is prime
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n + 1):
        if n % i == 0:
            return False

    # If no factors were found, return True
    return True
