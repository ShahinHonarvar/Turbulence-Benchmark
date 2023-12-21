
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the list of integers and check if each integer is not divisible by 86
    for i in my_list:
        if i % 86 != 0:
            # If the integer is not divisible by 86, add it to the result list
            result.append(i)

    # Return the result list

    return result
