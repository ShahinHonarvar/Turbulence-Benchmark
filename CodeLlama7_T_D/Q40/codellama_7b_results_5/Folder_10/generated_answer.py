
def return_n_smallest_chars(string, n):
    # create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # sort the list in descending order based on the ASCII value
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # return the top n characters from the sorted list
    return [char for (char, _) in sorted_list[:n]]
