
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the list and check if each element is not divisible by 93
    for i in range(45, 72):
        if my_list[i] % 93 != 0:
            result_list.append(my_list[i])

    # Return the resulting list of all integers not divisible by 93 from index 45 to index 72, both exclusive
    return result_list
