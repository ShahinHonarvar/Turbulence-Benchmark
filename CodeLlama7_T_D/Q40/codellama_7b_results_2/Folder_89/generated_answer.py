
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # Create a list of exactly 55 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_string[:55]
    return smallest_chars
