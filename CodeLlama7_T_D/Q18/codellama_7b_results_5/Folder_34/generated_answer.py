
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    current_index = 60
    # Loop through the list, starting from the specified index
    while current_index <= 200:
        # If the current element is divisible by either 9 or 11, add it to the sum
        if my_list[current_index] % 9 == 0 or my_list[current_index] % 11 == 0:
            sum += my_list[current_index]
        # Increment the current index by 1
        current_index += 1
    # Return the sum of all integers divisible by either 9 or 11 from index 60 to index 200, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
