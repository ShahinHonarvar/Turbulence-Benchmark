
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check for each element if it is a prime number or not
    for i in range(51, 87):
        if my_list[i] > 1:
            # If the element is a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    return composite_nums
