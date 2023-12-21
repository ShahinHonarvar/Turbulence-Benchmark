
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the list and check if each element is divisible by both -9 and -3
    for i in range(1, 8):
        if my_list[i] % -9 == 0 and my_list[i] % -3 == 0:
            result.append(my_list[i])

    # Return the list of all integers divisible by both -9 and -3 from index 1 to index 8, both inclusive
    return result
