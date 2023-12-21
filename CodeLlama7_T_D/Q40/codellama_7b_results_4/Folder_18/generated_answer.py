
def return_n_smallest_chars(s, n):
    # Sort the string in descending order based on ASCII values
    sorted_s = sorted(s, key=ord, reverse=True)
    # Create a list of exactly n characters from the sorted string
    smallest_chars = sorted_s[:n]
    return smallest_chars
