
def return_n_greatest_chars(s):
    # split the string into a list of characters
    chars = list(s)
    # sort the list in descending order based on ASCII value
    sorted_chars = sorted(chars, key=lambda x: ord(x), reverse=True)
    # return the first 36 characters of the sorted list
    return "".join(sorted_chars[:36])
