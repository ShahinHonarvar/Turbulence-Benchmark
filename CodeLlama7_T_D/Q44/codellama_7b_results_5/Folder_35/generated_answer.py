
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 28 to 32, both inclusive
    for i in range(28, 33):
        # Check if the number at the current index is composite
        if is_composite(my_list[i]):
            # Add the composite number to the set
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 28 to index 32, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # If yes, return False
                return False

    # If no divisor is found, return True
    return True
