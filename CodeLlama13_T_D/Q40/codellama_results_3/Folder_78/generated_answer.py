
def return_n_smallest_chars(string):
    chars = set(string)  # distinct characters of the string
    chars_list = list(chars)  # convert to a list
    sorted_chars = sorted(chars_list, key=ord)  # sort by ASCII value
    return sorted_chars[:43]  # return the first 43 elements
