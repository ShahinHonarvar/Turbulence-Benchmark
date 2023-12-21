
def all_ints_not_div_by_num(my_list):
    # Create a new list to store the results
    result_list = []

    # Iterate through the list of integers and check if each integer is not divisible by 16
    for i in range(50, 92):
        if my_list[i] % 16 != 0:
            result_list.append(my_list[i])

    # Return the list of all integers not divisible by 16 from index 50 to index 92, both exclusive
    return result_list
