
def sum_in_range(my_list):
    # Initialize sum variable
    sum = 0
    # Loop through the list and check if each integer is between 46 and 91
    for i in my_list:
        if 46 <= i <= 91:
            sum += i
    # Return the sum
    return sum
