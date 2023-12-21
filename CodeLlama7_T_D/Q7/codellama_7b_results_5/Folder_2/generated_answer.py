
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list and check if each element is even
    for i in range(15, 39 + 1):
        if my_list[i] % 2 == 0:
            # If the element is even, add it to the list of even integers
            even_ints.append(my_list[i])
    return even_ints
