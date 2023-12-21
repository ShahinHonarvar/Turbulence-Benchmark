
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the number is between index 51 and 86, both inclusive
        if (i >= 51) and (i <= 86):
            # Check if the number is composite using the Miller-Rabin primality test
            if miller_rabin(my_list[i]):
                # If the number is composite, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of composite numbers in the specified range
    return composite_nums

# Define the Miller-Rabin primality test function
def miller_rabin(n):
    # Base case: if n is smaller than 3, it is not prime
    if n < 3:
        return False

    # Find a witness value for Composite-ness
    witness = 2

    # Perform the Miller-Rabin primality test
    while (witness ** (n - 1)) % n != 1:
        if witness == (n - 1):
            return True

        witness += 1

    return False
