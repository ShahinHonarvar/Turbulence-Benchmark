
def return_n_smallest_chars(s, n):
    # Create a list of tuples containing the ASCII value and character for each character in the string
    char_list = [(ord(c), c) for c in s]
    # Sort the list in descending order based on the ASCII value
    char_list.sort(key=lambda x: x[0], reverse=True)
    # Return the top n characters from the sorted list
    return [tup[1] for tup in char_list[:n]]
