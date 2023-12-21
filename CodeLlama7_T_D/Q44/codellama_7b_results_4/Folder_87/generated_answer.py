 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Loop through the list and check if each element is a prime number or not
    for i in range(43, 52):
        # If the element is not a prime number, it is a composite number
        if my_list[i] != i:
            # Add the composite number to the set
            composite_nums.add(my_list[i])
    return composite_nums
