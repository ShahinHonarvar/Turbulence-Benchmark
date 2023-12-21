
def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort()  # sort the characters in ascending order
    return sorted(chars[:13], reverse=True)  # return the first 13 characters in descending order
