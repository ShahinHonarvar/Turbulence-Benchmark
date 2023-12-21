
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list of integers
    for i in range(13, 76):
        # Check if the current integer is not divisible by 44
        if my_list[i] % 44 != 0:
            # If it's not divisible, add it to the results list
            result.append(my_list[i])

    # Return the list of all integers not divisible by 44 from index 13 to index 76, both exclusive
    return result
