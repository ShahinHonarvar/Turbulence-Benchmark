
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list, starting from index 50
    for i in range(50, len(my_list)):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]
    return total
