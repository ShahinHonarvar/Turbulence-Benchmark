
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list of integers starting from index 34 to index 55, both inclusive
    for i in range(34, 56):
        # Check if the current element is even and append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
