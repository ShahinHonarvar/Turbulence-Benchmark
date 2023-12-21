
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the input list and check if each integer is not divisible by -27
    for i in range(36, 85 + 1):
        if my_list[i] % -27 != 0:
            results.append(my_list[i])

    # Return the list of all integers not divisible by -27 from index 36 to index 85, both exclusive
    return results
