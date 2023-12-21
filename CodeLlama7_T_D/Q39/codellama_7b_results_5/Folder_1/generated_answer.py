 def return_n_greatest_chars(s):
    # create a list of tuples containing the character and its ASCII value
    ascii_values = [(c, ord(c)) for c in s]
    # sort the list in descending order based on the ASCII values
    sorted_list = sorted(ascii_values, key=lambda x: x[1], reverse=True)
    # return the top 11 characters from the sorted list
    return [c for c, _ in sorted_list[:11]]
