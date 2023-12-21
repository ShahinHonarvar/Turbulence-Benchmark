
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate through the list from index 56 to 98 (inclusive)
    for i in range(56, 99):
        # Check if the number at the current index is composite
        if is_composite(my_list[i]):
            # If it is, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of composite numbers in the specified range
    return composite_numbers

# Function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the number is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True
