
def return_n_smallest_chars(string, n):
    # create a list of tuples containing the ASCII value and character for each character in the string
    char_list = [(ord(c), c) for c in string]
    # sort the list in descending order based on the first element (ASCII value)
    char_list.sort(key=lambda x: x[0], reverse=True)
    # return the top 82 characters from the sorted list
    return [char for (_, char) in char_list[:n]]
