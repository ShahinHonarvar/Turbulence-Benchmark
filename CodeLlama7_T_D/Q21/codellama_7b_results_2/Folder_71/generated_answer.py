
def all_ints_div_by_num(my_list, num):
    # Create an empty list to store the results
    result = []

    # Loop through the specified range of the input list
    for i in range(len(my_list[29:51])):
        # Check if the current element is divisible by the given number
        if my_list[i] % num == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
