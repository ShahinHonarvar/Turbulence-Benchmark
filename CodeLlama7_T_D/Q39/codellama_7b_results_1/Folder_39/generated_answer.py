
def return_n_greatest_chars(my_string):
    # create a list of tuples containing the character and its ASCII value
    char_ascii_list = [(char, ord(char)) for char in my_string]
    # sort the list by the ASCII value in descending order
    sorted_list = sorted(char_ascii_list, key=lambda x: x[1], reverse=True)
    # return the top 23 characters of the sorted list
    return [char for char, _ in sorted_list[:23]]
