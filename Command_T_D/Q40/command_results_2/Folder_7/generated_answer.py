import re
def return_n_smallest_chars(s):
    # Match all individual characters in the string
    matches = re.findall(r'([a-z])', s)
    # Sort the list of characters by their ASCII value
    characters = sorted(list(set(matches)), key=lambda x: ord(x))[:49]
    # Return the sorted list of characters
    return characters
