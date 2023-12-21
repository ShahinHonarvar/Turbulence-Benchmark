
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(22, 88 + 1):
        # Check if the current number is composite by dividing it by all the prime factors less than or equal to its square root
        is_composite = False
        for prime in my_list[i]:
            if my_list[i] % prime == 0:
                is_composite = True
                break

        # If the current number is composite, add it to the set of composite numbers
        if is_composite:
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
