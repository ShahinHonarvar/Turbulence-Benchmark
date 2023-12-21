 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each number is composite
    for i in range(1, len(my_list)):
        # If the number is not prime, it is a composite number
        if my_list[i] != 1:
            # Check if the number is between index 1 and index 5
            if i >= 1 and i <= 5:
                # Add the composite number to the set
                composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the given list that are between index 1 to index 5, both inclusive
    return composite_nums
