
def return_n_greatest_chars(s, n):
    # Create a list of tuples containing the character and its ASCII value
    chars = [(c, ord(c)) for c in s]
    # Sort the list by the ASCII values in descending order
    chars.sort(key=lambda x: x[1], reverse=True)
    # Return the top n characters from the sorted list
    return [c[0] for c in chars[:n]]
