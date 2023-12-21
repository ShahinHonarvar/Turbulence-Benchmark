
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check if each number is composite
    for i in range(13, 68 + 1):
        # If the number is not prime, it is a composite number
        if not my_list[i].is_prime():
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
