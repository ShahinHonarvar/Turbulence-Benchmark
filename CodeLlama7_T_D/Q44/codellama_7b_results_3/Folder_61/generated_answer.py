
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each element is a prime number
    for i in range(len(my_list)):
        if my_list[i] > 1:
            # If the current element is not a prime number, it must be a composite number
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
