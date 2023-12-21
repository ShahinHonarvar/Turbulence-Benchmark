
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0
    # Iterate over the list and check if each element is between 60 and 90
    for i in range(len(my_list)):
        if my_list[i] >= 60 and my_list[i] <= 90:
            sum += my_list[i]
    return sum
