
def sum_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    
    # Iterate through the list and append all even integers to the list
    for i in range(25, 87 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    
    # Return the sum of the even integers
    return sum(even_ints) or 0
