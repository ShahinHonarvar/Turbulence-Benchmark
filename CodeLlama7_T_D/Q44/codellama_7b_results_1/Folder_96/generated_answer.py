
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the specified range
    start = my_list.index(60)
    end = my_list.index(200)
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list in the specified range
    for i in range(start, end + 1):
        # Check if the current element is a prime number
        if my_list[i] == 2 or (my_list[i] > 2 and my_list[i] % 2 != 0)):
            # If it is a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
