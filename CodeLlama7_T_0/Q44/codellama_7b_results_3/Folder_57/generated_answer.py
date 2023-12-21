
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(25, 60):
        # Check if the current number is divisible by any number between 1 and itself
        for j in range(1, i + 1):
            if i % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_nums.add(i)
                break

    return composite_nums
