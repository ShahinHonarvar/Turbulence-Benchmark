
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the specified range of the input list
    for i in range(20, 51):
        # Check if the current element is not divisible by -48
        if my_list[i] % -48 != 0:
            # If it is not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
