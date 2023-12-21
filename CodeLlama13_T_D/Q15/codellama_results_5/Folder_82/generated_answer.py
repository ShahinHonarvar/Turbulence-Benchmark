
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum of odd integers
    sum = 0
    
    # Iterate through the list and check if each integer is odd
    for i in range(20, 201, 2):
        if my_list[i] % 2 == 1:
            sum += my_list[i]
            
    # Return the sum of all odd integers
    return sum
