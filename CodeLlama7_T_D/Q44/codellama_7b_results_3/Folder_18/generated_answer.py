
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 25 to index 87, both inclusive
    for i in range(25, 88):
        # Check if the current element is a composite number
        if is_composite(my_list[i]):
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 25 to index 87, both inclusive
    return composite_nums

# Check if a number is a composite number
def is_composite(n):
    # If the number is less than 1 or greater than 1000, it is not a valid input
    if n < 1 or n > 1000:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    # If none of the above conditions are met, the number is not a composite number
    return False
