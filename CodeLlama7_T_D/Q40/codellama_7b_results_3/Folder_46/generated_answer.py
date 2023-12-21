
def return_n_smallest_chars(string):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x), reverse=True)
    # Create a list of exactly 54 characters from the sorted string
    n_smallest_chars = sorted_string[:54]
    return n_smallest_chars
