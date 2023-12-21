
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is prime or not
        if my_list[i] > 1:
            # If the current number is prime, check if it is between indices 0 to 5, both inclusive
            if i >= 0 and i <= 5:
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 0 to index 5, both inclusive
    return composite_nums
