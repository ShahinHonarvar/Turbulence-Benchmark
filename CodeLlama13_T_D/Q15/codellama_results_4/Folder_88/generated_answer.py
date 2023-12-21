
def sum_odd_ints_inclusive(my_list):
    # initialize an empty list to store the odd integers
    odd_ints = []
    
    # iterate over the list and append any odd integers to the list
    for i in range(4, 9):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
            
    # return the sum of all odd integers in the list
    return sum(odd_ints)
