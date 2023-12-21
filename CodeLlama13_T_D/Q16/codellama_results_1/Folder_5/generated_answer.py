
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum of even integers
    sum_even = 0
    # Iterate over the list and check if each integer is even
    for i in range(8, 10):
        if my_list[i] % 2 == 0:
            sum_even += my_list[i]
    return sum_even
