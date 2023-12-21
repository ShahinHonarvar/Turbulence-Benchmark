
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the list and check if each element is divisible by both -6 and 4
    for i in range(len(my_list)):
        if my_list[i] % (-6) == 0 and my_list[i] % 4 == 0:
            # If the element is divisible by both -6 and 4, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
