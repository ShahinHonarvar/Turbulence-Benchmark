
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 64 and index 66 (inclusive)
        if i >= 64 and i <= 66:
            # Check if the current number is composite using the 'is_composite' function defined below
            if is_composite(my_list[i]):
                # If the current number is composite, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 64 and index 66 (inclusive), or an empty set if no such numbers exist in the list
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is equal to 1 or itself
    if n == 1 or n == 0:
        # Return False if the condition is met
        return False

    # Check if any of the numbers from 2 to the square root of n are divisible by n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # Return True if any such number is found
            return True

    # Return False if no such number is found
    return False
