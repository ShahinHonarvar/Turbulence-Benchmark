
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the input list
    for i in range(len(my_list)):
        # Check if the current element is divisible by -80
        if my_list[i] % (-80) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
