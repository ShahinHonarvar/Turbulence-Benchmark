
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the sublist
    first_idx = my_list.index(4)
    last_idx = my_list.index(4)
    # Create an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the sublist and check if each element is a composite number
    for i in range(first_idx, last_idx + 1):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_nums.add(my_list[i])
    # Return the set of composite numbers in the specified range
    return composite_nums
