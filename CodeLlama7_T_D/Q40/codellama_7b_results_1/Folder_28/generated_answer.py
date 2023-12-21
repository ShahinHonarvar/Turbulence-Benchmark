
def return_n_smallest_chars(s):
    # Sort the string in ascending order
    sorted_s = sorted(s)
    # Return the first 3 characters of the sorted string
    return sorted_s[:3]
