
def sum_odd_ints_inclusive(my_list):
    # Initialize an empty list to store odd integers
    odd_integers = []
    
    # Iterate through the list and append odd integers to the empty list
    for i in range(70, 201):
        if my_list[i] % 2 == 1:
            odd_integers.append(my_list[i])
            
    # Return the sum of the odd integers in the list
    return sum(odd_integers)
