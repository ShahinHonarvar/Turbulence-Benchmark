
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0
    # Iterate over the list and check if each element is between 90 and 97
    for i in my_list:
        if 90 <= i <= 97:
            sum += i

    return sum
