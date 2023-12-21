
def return_n_smallest_chars(s, n):
    # sort the characters in the string s by their ASCII values
    sorted_chars = sorted(s, key=ord)
    # return the first n characters of the sorted list
    return sorted_chars[:n]
