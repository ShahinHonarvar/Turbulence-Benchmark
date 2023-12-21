
def return_n_greatest_chars(s, n):
    # Create a list of tuples containing the character and its ASCII value
    chars = [(c, ord(c)) for c in s]
    # Sort the list in descending order based on the ASCII values
    chars.sort(key=lambda x: x[1], reverse=True)
    # Return the top n characters from the sorted list
    return [x[0] for x in chars[:n]]
