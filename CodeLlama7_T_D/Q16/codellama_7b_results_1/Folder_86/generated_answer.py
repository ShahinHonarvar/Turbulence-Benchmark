
def sum_even_ints_inclusive(my_list):
    # Initialize an empty list for the even integers
    even_integers = []
    # Iterate over the input list and append all even integers to the empty list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_integers.append(my_list[i])
    # Initialize a variable to store the sum of the even integers
    total = 0
    # Iterate over the list of even integers and calculate the sum
    for i in range(len(even_integers)):
        total += even_integers[i]
    return total
