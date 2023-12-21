
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate over the list and check if each element is even
    for i in range(28, 33):
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    
    # Return the sum
    return sum
