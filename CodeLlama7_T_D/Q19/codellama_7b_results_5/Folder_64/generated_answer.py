
def all_ints_not_div_by_num(my_list):
    # Create a new list to store the result
    result = []

    # Iterate over the input list and check if each element is not divisible by 2
    for i in my_list:
        if i % 2 != 0:
            result.append(i)

    # Return the result list
    return result
