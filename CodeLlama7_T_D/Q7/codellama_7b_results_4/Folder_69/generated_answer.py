
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list and append the even integers to the empty list
    for i in range(32, 35+1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
