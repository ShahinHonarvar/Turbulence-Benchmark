
def all_ints_div_by_both_two_nums(my_list):
    # Check if the specified range contains any integers divisible by both -37 and -26
    for i in range(68, 100 + 1):
        if my_list[i] % (-37) == 0 and my_list[i] % (-26) == 0:
            # If the current element is divisible by both -37 and -26, add it to the result list
            result.append(my_list[i])
    return result
