
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for sum and counter
    total = 0
    count = 0

    # Iterate through list from index 58 to index 75, both inclusive
    for i in range(58, 76):
        # Check if current element is divisible by either 72 or 62
        if my_list[i] % 72 == 0 or my_list[i] % 62 == 0:
            # Increment sum and counter if condition is met
            total += my_list[i]
            count += 1

    # Return sum of all integers divisible by either 72 or 62 from index 58 to index 75, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
