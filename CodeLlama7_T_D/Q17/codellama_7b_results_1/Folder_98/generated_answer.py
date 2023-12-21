
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the input list and check if each element is divisible by both -1 and 13
    for i in range(len(my_list)):
        if my_list[i] % -1 == 0 and my_list[i] % 13 == 0:
            # If the element is divisible by both -1 and 13, append it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
