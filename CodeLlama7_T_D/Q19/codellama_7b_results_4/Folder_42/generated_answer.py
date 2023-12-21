
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the list and check if each integer is not divisible by 90
    for i in range(11, 56):
        if my_list[i] % 90 != 0:
            # If the integer is not divisible by 90, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
