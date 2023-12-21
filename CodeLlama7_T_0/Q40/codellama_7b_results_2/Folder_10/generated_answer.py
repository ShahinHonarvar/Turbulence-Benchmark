
def return_n_smallest_chars(string, n=88):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(string, key=ord, reverse=True)
    # Return the top n characters of the sorted string
    return sorted_string[:n]
