
def return_n_smallest_chars(string):
    # create a list of all distinct characters in the string
    chars = set(string)
    # sort the list by ASCII value, descending order
    sorted_chars = sorted(chars, key=ord, reverse=True)
    # return a list of 29 characters from the sorted list
    return sorted_chars[:29]
