
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list and check if each element is between 5 and 9, both inclusive
    for i in my_list:
        if 5 <= i <= 9:
            total += i

    # Return the sum

    return total
