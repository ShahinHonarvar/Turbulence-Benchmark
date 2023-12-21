
def return_n_smallest_chars(string, n):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x), reverse=True)
    # Return the first n characters of the sorted string
    return sorted_string[:n]
