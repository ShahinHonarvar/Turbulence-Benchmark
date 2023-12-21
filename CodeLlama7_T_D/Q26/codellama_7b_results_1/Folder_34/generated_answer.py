
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list and check if each element is between 4 and 7
    for i in my_list:
        if 4 <= i <= 7:
            sum += i

    return sum
