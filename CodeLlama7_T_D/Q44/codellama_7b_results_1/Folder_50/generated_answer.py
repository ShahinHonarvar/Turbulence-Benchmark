
def composite_nums_between_indices(my_list):
    # Check if the list is valid
    if not my_list or len(my_list) < 57:
        return set()

    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the elements in the range [56, 57]
    for i in range(56, 58):
        # Check if the current element is a prime number
        if my_list[i] == 1:
            continue

        # Iterate over the factors of the current element
        for j in range(1, int(my_list[i]) + 1):
            # Check if the current factor is a prime number
            if my_list[i] % j == 0 and my_list[i - 1] == 1:
                composite_nums.add(j)

    return composite_nums
