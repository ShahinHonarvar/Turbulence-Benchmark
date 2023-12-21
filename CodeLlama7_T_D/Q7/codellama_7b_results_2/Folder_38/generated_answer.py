
def all_even_ints_inclusive(my_list):
    # Define a lambda function to check if an integer is even
    is_even = lambda x: x % 2 == 0
    # Use the filter() method to apply the lambda function to each element in the list
    filtered_list = list(filter(is_even, my_list))
    # Define a slice of the list from index 22 to index 63, both inclusive
    slice_list = filtered_list[22:64]
    return slice_list
