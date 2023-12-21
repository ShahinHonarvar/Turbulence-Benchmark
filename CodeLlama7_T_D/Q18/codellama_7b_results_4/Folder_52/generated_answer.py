
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for sum and divisible integers count
    sum = 0
    count = 0
    # Iterate through the list, starting from index 48
    for i in range(48, len(my_list)):
        # Check if current integer is divisible by either 88 or 58
        if my_list[i] % 88 == 0 or my_list[i] % 58 == 0:
            # If it is, add it to the sum and increment the count
            sum += my_list[i]
            count += 1

    # Return the sum of all divisible integers, or 0 if no such integers exist in the specified range
    return sum if count > 0 else 0
