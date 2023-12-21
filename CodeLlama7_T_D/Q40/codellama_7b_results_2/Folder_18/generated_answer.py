
def return_n_smallest_chars(s, n):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(s, key=lambda x: ord(x), reverse=True)
    # Return the first n characters of the sorted string
    return sorted_string[:n]
