
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Loop through the list of integers and check if each integer is not divisible by -32
    for i in range(19, 94):
        if my_list[i] % -32 != 0:
            result_list.append(my_list[i])

    # Return the list of all integers not divisible by -32 from index 19 to index 94, both exclusive
    return result_list
