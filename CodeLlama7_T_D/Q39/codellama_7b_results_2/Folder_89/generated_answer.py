
def return_n_greatest_chars(s, n):
    # Create a list of tuples containing the character and its ASCII value
    chars = [(c, ord(c)) for c in s]
    # Sort the list in descending order based on the ASCII values
    sorted_chars = sorted(chars, key=lambda x: -x[1])
    # Return the top n characters from the sorted list
    return [c[0] for c in sorted_chars[:n]]
