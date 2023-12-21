import re
def return_n_smallest_chars(s):
    # Find all unique characters in the string.
    chars = re.findall(r'[A-Z]+', s)
    # Sort them by their ASCII values and keep only the first 46.
    return sorted(chars[:46])
