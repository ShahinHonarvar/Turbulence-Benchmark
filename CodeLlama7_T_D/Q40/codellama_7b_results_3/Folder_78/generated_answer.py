
def return_n_smallest_chars(s):
    # Sort the string in descending order based on ASCII values
    s = sorted(s, key=ord, reverse=True)
    # Return the first 43 characters of the sorted string
    return s[:43]
