
def return_n_smallest_chars(s, n=55):
    # Sort the string in ascending order based on ASCII values
    sorted_s = sorted(s, key=ord)
    # Return the first n elements of the sorted list
    return sorted_s[:n]
