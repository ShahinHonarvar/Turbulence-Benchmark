
def return_n_greatest_chars(string):
    char_list = list(set(string))  # create a set of distinct characters in the string
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True)  # sort the list by ASCII value in descending order
    return sorted_char_list[:14]  # return the first 14 elements of the sorted list
