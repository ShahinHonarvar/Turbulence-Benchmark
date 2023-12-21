
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the input list and check if each integer is not divisible by 84
    for i in range(43, 77):
        if my_list[i] % 84 != 0:
            results.append(my_list[i])

    # Return the list of all integers not divisible by 84 from index 43 to index 77, both exclusive
    return results
