
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(my_string, key=lambda x: ord(x))
    # Create a list of exactly 44 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_string[:44]
    return smallest_chars
