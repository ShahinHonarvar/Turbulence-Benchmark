
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum of even integers
    even_sum = 0
    
    # Iterate through the list and check if each integer is even
    for i in range(31, 35):
        if my_list[i] % 2 == 0:
            even_sum += my_list[i]
    
    # Return the sum of even integers
    return even_sum
