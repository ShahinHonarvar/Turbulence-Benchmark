
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(37, 76 + 1):
        # Check if the current number is composite by dividing it by all the prime factors of it
        is_composite = False
        for j in range(2, int(my_list[i] ** 0.5) + 1):
            if my_list[i] % j == 0:
                is_composite = True
                break

        # If the current number is composite, add it to the set of composite numbers
        if is_composite:
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
