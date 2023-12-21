
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate through the list and check if each integer is divisible by both -31 and 13
    for i in range(90, 200 + 1):
        if my_list[i] % (-31) == 0 and my_list[i] % (13) == 0:
            results.append(my_list[i])

    # Return the list of all integers divisible by both -31 and 13 from index 90 to index 200, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return results
