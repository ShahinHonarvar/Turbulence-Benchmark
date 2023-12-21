
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of indices in the input list
    for i in range(81, 86 + 1):

        # Check if the current element is not divisible by 77
        if my_list[i] % 77 != 0:

            # If it is not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
