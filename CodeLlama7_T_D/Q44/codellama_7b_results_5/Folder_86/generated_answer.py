
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # If the current number is greater than 1 and is divisible by any number between 2 and the square root of the current number
        if my_list[i] > 1 and all(my_list[i] % j == 0 for j in range(2, int(my_list[i]) ** 0.5 + 1))):
            # Add the current number to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 43 and index 86, both inclusive
    return composite_nums
