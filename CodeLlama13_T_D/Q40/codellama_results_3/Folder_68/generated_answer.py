
def return_n_smallest_chars(string):
    chars = set(string)  # get distinct characters as a set
    sorted_chars = sorted(chars, key=ord)  # sort the characters by their ASCII value in descending order
    return sorted_chars[:89]  # return the first 89 characters of the sorted list
