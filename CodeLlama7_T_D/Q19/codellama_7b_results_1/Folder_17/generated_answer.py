
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the list and check if each element is not divisible by 84
    for i in range(39, 57):
        if my_list[i] % 84 != 0:
            result.append(my_list[i])

    # Return the result list
    return result
