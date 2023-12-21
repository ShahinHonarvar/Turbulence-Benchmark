
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list from index 533 to index 605 (both inclusive)
    for i in range(533, 605 + 1):
        # Check if the current number is a prime number
        if my_list[i] == 1:
            # If it is not a prime number, then it is a composite number
            composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
