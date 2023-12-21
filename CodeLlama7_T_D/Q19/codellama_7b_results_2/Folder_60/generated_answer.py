
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the input list and check if each element is not divisible by -99
    for i in range(len(my_list)):
        if my_list[i] % -99 != 0:
            result_list.append(my_list[i])

    # Return the list of all integers not divisible by -99 from index 63 to index 73, both exclusive
    return result_list
