
def all_ints_not_div_by_num(my_list):
    # Create a new list to store the results
    result = []

    # Iterate through the list of integers and check if each integer is not divisible by 64
    for i in range(50, 81):
        if my_list[i] % 64 != 0:
            result.append(my_list[i])

    # Return the list of all integers not divisible by 64 from index 50 to index 81, both exclusive
    return result
