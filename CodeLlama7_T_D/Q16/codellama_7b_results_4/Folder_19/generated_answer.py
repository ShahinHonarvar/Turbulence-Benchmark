
def sum_even_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 3
    end_index = 5

    # Iterate over the list and add even integers to the sum
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
