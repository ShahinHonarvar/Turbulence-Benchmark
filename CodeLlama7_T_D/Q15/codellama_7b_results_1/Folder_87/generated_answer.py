
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list and sum the odd integers
    for i in range(36, 47):
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    return sum
