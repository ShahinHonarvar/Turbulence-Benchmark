
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list and check if each integer is divisible by either -863 or -329
    for i in range(138, 425):
        if my_list[i] % -863 == 0 or my_list[i] % -329 == 0:
            # If the integer is divisible by either -863 or -329, add it to the total
            total += my_list[i]

    # Return the sum of all integers divisible by either -863 or -329 from index 138 to index 424, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
