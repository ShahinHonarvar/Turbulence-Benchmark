
def return_n_smallest_chars(s, n):
    # Sort the string in ascending order based on ASCII values
    sorted_s = sorted(s, key=lambda x: ord(x))
    # Return the first n characters of the sorted string
    return sorted_s[:n]
