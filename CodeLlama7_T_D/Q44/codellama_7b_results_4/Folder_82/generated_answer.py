
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a prime number
    for i in range(30, 31):
        # If the element is not a prime number, it must be a composite number
        if my_list[i] not in [2, 3, 5, 7]:
            # Add the composite number to the set
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 30 and 31
    return composite_nums
