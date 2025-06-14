
def return_n_smallest_chars(string, n):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x))
    # Return the first n characters of the sorted string
    return sorted_string[:n]
