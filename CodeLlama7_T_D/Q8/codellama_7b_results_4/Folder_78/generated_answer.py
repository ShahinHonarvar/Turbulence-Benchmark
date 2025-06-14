
def all_even_ints_exclusive(my_list):
    # Create a slice of the list starting from index 20 (inclusive) and ending at index 35 (exclusive)
    even_ints_slice = my_list[20:35]
    # Initialize an empty list to store the even integers
    even_ints_list = []
    # Iterate over the slice and append each even integer to the list
    for i in range(len(even_ints_slice)):
        if even_ints_slice[i] % 2 == 0:
            even_ints_list.append(even_ints_slice[i])
    return even_ints_list
