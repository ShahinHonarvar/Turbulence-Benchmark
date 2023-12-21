
def return_n_smallest_chars(s):
    # Sort the string in ascending order based on ASCII values
    s = sorted(s, key=ord)
    # Return the first 60 characters of the sorted string
    return s[:60]
