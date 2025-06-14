
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the range of prime numbers less than x
    for i in range(2, x):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the leading leftmost digit of i can be successively removed and still result in a prime number
            while True:
                # Get the next rightmost digit of i
                digit = str(i)[-1]

                # Remove the rightmost digit of i
                i //= 10

                # Check if the resulting number is prime
                if not is_prime(i):
                    break

            # If the leading leftmost digit of i can be successively removed and still result in a prime number, then add it to the results list
            results.append(i)

    # Sort the results list in ascending order
    results.sort()

    # Return the sorted results list
    return results
