
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(1, len(my_list)):
        # Check if the number is divisible by any other number in the range
        for j in range(2, i + 1):
            if my_list[i] % j == 0:
                composite_nums.add(my_list[i])

    return composite_nums
