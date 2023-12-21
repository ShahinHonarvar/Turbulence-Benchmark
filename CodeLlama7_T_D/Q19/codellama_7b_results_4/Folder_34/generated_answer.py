
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list of integers and check if each integer is not divisible by 9
    for i in range(len(my_list)):
        if my_list[i] % 9 != 0:
            # If the integer is not divisible by 9, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
