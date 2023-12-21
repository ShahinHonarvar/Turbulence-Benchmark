
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 90 and index 200, both inclusive
        if 90 <= i <= 200:
            # Check if the current number is composite using the 'is_composite' function
            if is_composite(my_list[i]):
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 90 and index 200, both inclusive
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                # Return False if i divides n without leaving a remainder
                return False

    # If the number is greater than 1, return True
    return True
