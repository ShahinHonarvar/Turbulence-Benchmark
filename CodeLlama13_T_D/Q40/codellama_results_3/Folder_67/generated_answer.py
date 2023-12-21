
def return_n_smallest_chars(distinct_char_string):
    char_list = list(set(distinct_char_string))  # create a list of distinct characters from the string
    sorted_char_list = sorted(char_list, key=lambda x: ord(x))  # sort the list in ascending order by ASCII value
    return sorted_char_list[:66]  # return the first 66 elements of the sorted list
