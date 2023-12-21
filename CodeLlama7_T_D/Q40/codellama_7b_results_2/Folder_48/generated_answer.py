
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(my_string, key=ord)
    # Create a list of exactly 12 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_string[:12]
    return smallest_chars
