
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 15 and 39 (inclusive)
        if 15 <= i <= 39:
            # If the current number is prime, add it to the set of composite numbers
            if my_list[i] == 2 or my_list[i] % 2 != 0:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 15 to index 39 (inclusive)
    return composite_nums
