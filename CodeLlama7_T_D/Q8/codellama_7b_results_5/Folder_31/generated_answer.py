
def all_even_ints_exclusive(my_list):
    # Define a lambda function to check if an integer is even
    is_even = lambda x: x % 2 == 0
    # Use list comprehension to filter the list for even integers in the specified range
    return [x for x in my_list[87:95] if is_even(x)]
