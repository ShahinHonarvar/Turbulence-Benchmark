
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(my_string, key=lambda x: ord(x))
    # Create a list of exactly 55 characters from the sorted string
    smallest_chars = sorted_string[:55]
    return smallest_chars
