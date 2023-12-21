
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list of positive integers
    for i in range(262, 747):
        # Check if the current number is divisible by any number between 1 and itself inclusive
        for j in range(1, i + 1):
            if i % j == 0:
                composite_nums.add(i)
                break

    return composite_nums
