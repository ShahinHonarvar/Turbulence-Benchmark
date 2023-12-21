
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(29, 93 + 1):
        # If the number at index i is composite, add it to the set
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 29 to index 93, both inclusive
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # If n is less than or equal to 1, it is not composite
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i, it is not composite
        if n % i == 0:
            return False

    # If no factors other than the number itself have been found, the number is composite
    return True
