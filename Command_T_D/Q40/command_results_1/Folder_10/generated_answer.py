import re
def return_n_smallest_chars(s):
    # find distinct characters in the string
    distinct_chars = re.findall(r'[A-Z][^A-Z]*', s)
    # sort the distinct characters in descending order
    distinct_chars.sort(key=lambda x: ord(x))
    # return the first 88 distinct characters
    return distinct_chars[:88]
