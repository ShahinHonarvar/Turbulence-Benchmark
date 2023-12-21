 def return_n_smallest_chars(string):
    # create a list of all characters in the string
    char_list = list(string)
    # sort the list in descending order based on the ASCII values of each character
    char_list.sort(key=ord, reverse=True)
    # return the top 27 characters from the sorted list
    return char_list[:27]
