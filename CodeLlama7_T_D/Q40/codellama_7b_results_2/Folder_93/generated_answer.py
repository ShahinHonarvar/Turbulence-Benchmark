
def return_n_smallest_chars(s):
    # Sort the string in descending order based on ASCII values
    sorted_s = sorted(s, key=ord, reverse=True)
    # Return the first 77 characters of the sorted string
    return sorted_s[:77]
