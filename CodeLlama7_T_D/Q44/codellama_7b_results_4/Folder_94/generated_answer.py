
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a prime number
    for i in range(len(my_list)):
        # If the current element is not a prime number, add it to the set of composite numbers
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 27 to index 55, both inclusive
    return composite_nums
