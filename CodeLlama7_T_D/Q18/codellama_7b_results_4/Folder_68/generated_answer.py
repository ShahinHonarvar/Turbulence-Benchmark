
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 7

    # Iterate over the list, starting at index 7
    while i < len(my_list):
        # If the current element is divisible by either 5 or 7, add it to the sum
        if my_list[i] % 5 == 0 or my_list[i] % 7 == 0:
            sum += my_list[i]

        # Increment the index variable
        i += 1

    # Return the sum of all integers divisible by either 5 or 7 from index 7 to index 7, both inclusive
    return sum
