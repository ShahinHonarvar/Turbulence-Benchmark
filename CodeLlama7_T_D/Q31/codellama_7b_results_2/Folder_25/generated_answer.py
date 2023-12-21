
def if_perfect_num(my_list):
    # Check if the list has at least 90 elements
    if len(my_list) < 90:
        return False

    # Calculate the sum of the first 100 perfect squares
    sum = 0
    for i in range(1, 101):
        sum += (i ** 2)

    # Return true if the integer at index 90 is equal to the calculated sum
    return my_list[90] == sum
