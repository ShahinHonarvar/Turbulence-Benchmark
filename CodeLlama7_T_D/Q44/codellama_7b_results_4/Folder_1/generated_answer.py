
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the elements of the list
    for i in range(len(my_list)):
        # If the element is a prime number, continue to the next iteration
        if my_list[i] == 1:
            continue

        # Check if the element is between index 69 and index 83 (inclusive)
        if i >= 69 and i <= 83:
            # If it is, check if it is a composite number
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % j == 0:
                    # If it is a composite number, add it to the set of composite numbers
                    composite_nums.add(my_list[i])

    # Return the set of composite numbers found in the specified range
    return composite_nums
