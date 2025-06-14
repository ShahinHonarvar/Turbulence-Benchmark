
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range of indices and the sum
    start = 46
    end = 91
    total = 0

    # Iterate over the list within the specified range
    for i in my_list[start:end+1]:
        # Check if the current integer is divisible by either 67 or 15
        if i % 67 == 0 or i % 15 == 0:
            # If it is, add it to the sum
            total += i

    # Return the sum of all integers divisible by either 67 or 15 within the specified range, or 0 if there are no such integers
    return total
