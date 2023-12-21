
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate over the list and check if each element is not divisible by 86
    for i in range(15, 57):
        if my_list[i] % 86 != 0:
            result_list.append(my_list[i])

    # Return the list of all integers not divisible by 86 from index 15 to index 57, both exclusive
    return result_list
