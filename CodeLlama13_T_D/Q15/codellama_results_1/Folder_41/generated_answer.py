
def sum_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the input list and append odd integers to the list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 1:
            odd_ints.append(my_list[i])
    # Calculate the sum of the odd integers using built-in sum function
    return sum(odd_ints)
