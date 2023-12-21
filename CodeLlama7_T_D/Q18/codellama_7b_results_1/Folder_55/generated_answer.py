
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    total = 0
    current_index = 0
    # Loop through the list of integers, starting from the first element
    for i in range(len(my_list)):
        # Check if the current element is divisible by either 10 or 100
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:
            # If it is, add it to the sum and increment the current index
            total += my_list[i]
            current_index += 1
    # Return the sum of all integers divisible by either 10 or 100 from index 0 to index 9, both inclusive
    return total
