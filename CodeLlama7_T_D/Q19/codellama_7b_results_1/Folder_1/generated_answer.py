
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list and check if each element is not divisible by -69
    for i in range(21, 70):
        if my_list[i] % -69 != 0:
            result.append(my_list[i])

    # Return the results
    return result
