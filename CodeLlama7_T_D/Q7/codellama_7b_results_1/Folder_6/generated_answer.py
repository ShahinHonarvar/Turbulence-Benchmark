
def all_even_ints_inclusive(my_list):
    # Define a lambda function to check if an integer is even
    is_even = lambda x: x % 2 == 0
    # Use the filter() method to find all even integers in the specified range
    return list(filter(is_even, my_list[10:66+1])) or []
