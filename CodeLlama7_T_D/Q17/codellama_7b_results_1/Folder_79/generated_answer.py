
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list and check if each element is divisible by both -3 and 6. If it is, append it to the result list.
    for i in range(8, 10):
        if my_list[i] % (-3) == 0 and my_list[i] % (6) == 0:
            result.append(my_list[i])

    # Return the result list
    return result
