
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(35, 49 + 1):
        # Check if the current number is a prime number
        if my_list[i] == 1:
            # If it is not a prime number, it must be a composite number
            composite_nums.add(my_list[i])

    return composite_nums
