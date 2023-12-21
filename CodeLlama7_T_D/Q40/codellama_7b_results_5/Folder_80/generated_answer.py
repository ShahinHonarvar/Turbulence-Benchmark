
def return_n_smallest_chars(s):
    # Sort the string in ascending order based on ASCII values
    sorted_s = sorted(s)
    # Return the first 35 characters of the sorted string
    return sorted_s[:35]
