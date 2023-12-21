
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is composite
        if is_composite(my_list[i]):
            # If it is, check if it is between indices 30 and 87 (inclusive)
            if 30 <= i <= 87:
                # If it is, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 30 and 87 (inclusive)
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the range of numbers from 2 to n-1 (inclusive)
        for i in range(2, n):
            # Check if i divides into n without a remainder
            if n % i == 0:
                # If it does, return False (n is not composite)
                return False

    # If we reach this point, then n must be composite
    return True
