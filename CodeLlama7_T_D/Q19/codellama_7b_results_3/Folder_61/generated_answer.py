
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the list of integers and check if each integer is not divisible by -6
    for i in range(len(my_list)):
        if my_list[i] % -6 != 0:
            result.append(my_list[i])

    # Return the list of all integers not divisible by -6 from index 0 to index 6, both exclusive
    return result
