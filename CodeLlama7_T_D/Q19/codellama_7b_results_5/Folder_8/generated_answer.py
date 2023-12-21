
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate through the list of integers, starting at index 17 and ending at index 88 (exclusive)
    for i in range(17, 88):

        # Check if the current integer is not divisible by -75
        if my_list[i] % -75 != 0:

            # If it is not divisible, add it to the results list
            results.append(my_list[i])

    # Return the results list
    return results
