
def return_n_greatest_chars(string):
    char_list = list(set(string))  # create a set of distinct characters from the string
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:29]  # sort the list in descending order and get the first 29 elements
    return "".join(sorted_char_list)  # join the sorted characters and return them as a string
