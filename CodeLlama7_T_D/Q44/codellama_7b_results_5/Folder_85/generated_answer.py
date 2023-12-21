
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 3 and 5 (inclusive)
        if i >= 3 and i <= 5:
            # Check if the current number is composite
            if is_composite(my_list[i]):
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 3 to index 5 (inclusive)
    return composite_nums

def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is less than or equal to 1, return True
    return True
