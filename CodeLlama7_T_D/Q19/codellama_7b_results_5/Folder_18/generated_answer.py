
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the specified range of indices in the input list
    for i in range(35, 98):

        # Check if the current element is not divisible by 41
        if my_list[i] % 41 != 0:

            # If it is not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
