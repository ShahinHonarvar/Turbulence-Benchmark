
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is not divisible by -97
        if my_list[i] % -97 != 0:
            # If it is not, add it to the result list
            result.append(my_list[i])

    return result
