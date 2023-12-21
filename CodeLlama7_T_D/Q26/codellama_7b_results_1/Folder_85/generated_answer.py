
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate through the list and check if each element is between 6 and 7
    for i in my_list:
        if 6 <= i <= 7:
            sum += i

    return sum
