
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the range
    start_index = my_list.index(62)
    end_index = my_list.index(78) + 1
    # Create an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list within the specified range
    for i in range(start_index, end_index):
        # Check if the number is composite by dividing it by all the prime factors of its square root
        is_composite = False
        for prime in range(2, int(math.sqrt(my_list[i])) + 1)):
            if my_list[i] % prime == 0:
                is_composite = True
                break

        # If the number is composite, add it to the set of composite numbers
        if is_composite:
            composite_nums.add(my_list[i])

    # Return the set of composite numbers within the specified range
    return composite_nums
