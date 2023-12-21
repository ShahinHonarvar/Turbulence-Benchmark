
def composite_nums_between_indices(my_list):
    # Check if the input is a list and not empty
    if not isinstance(my_list, list) or len(my_list) == 0:
        raise ValueError("The input must be a non-empty list")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements of the list and check if they are composite
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
                    break
    # Return the set of all composite numbers in the specified range
    return composite_nums
