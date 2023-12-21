
def return_n_smallest_chars(s):
    # create a list of tuples containing (char, ASCII value)
    char_ascii_list = [(c, ord(c)) for c in s]
    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_ascii_list, key=lambda x: x[1], reverse=True)
    # return the top 87 characters in the sorted list
    return [c for c, _ in sorted_list[:87]]
