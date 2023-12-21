
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(62, 100):
        # Check if the current number is divisible by any number between 2 and itself
        for j in range(2, i + 1):
            if i % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_nums.add(i)

    # Return the set of all composite numbers between index 62 and index 99, both inclusive
    return composite_nums
