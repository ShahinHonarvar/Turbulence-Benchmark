
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list and check if each element is between 34 and 69, both inclusive
    for num in my_list:
        if 34 <= num <= 69:
            total += num

    return total
