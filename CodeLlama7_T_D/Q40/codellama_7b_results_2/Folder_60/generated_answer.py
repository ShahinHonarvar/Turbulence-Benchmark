
def return_n_smallest_chars(s, n):
    # Sort the characters of the input string in ascending order based on their ASCII values
    sorted_s = sorted(s, key=ord)
    # Return the first n elements of the sorted list
    return sorted_s[:n]
