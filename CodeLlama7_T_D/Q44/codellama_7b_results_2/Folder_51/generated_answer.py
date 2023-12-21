
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(1, len(my_list)):
        # Check if the current number is a composite number
        if my_list[i] > 1 and my_list[i] % 2 != 0:
            # If it is a composite number, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 1 and index 8, both inclusive
    return composite_nums
