
def sum_even_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 30
    end_index = 48
    # Iterate through the list and add even integers to the sum
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
