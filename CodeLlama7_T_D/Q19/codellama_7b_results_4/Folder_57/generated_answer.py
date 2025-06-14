
def all_ints_not_div_by_num(my_list):
    # Define the range of indices to consider
    start = 56
    end = 88
    # Initialize an empty list to store the result
    result = []
    # Iterate over the specified range of indices
    for i in range(start, end):
        # Check if the current integer is not divisible by -59
        if my_list[i] % -59 != 0:
            # If it is not divisible, add it to the result list
            result.append(my_list[i])
    # Return the result list
    return result
