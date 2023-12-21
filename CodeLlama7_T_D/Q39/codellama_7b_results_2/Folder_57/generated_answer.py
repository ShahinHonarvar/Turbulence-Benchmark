
def return_n_greatest_chars(string, n=29):
    # create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)[:n]
    # return the top n characters with the greatest ASCII values
    return [char for char, _ in sorted_list]
