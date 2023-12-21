
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the list and check if each integer is not divisible by -72
    for i in range(len(my_list)):
        if my_list[i] % -72 != 0:
            result_list.append(my_list[i])

    # Return the list of all integers not divisible by -72 from index 24 to index 45, both exclusive
    return result_list
