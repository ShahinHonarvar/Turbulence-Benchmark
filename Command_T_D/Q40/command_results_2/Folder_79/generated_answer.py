import re
def return_n_smallest_chars(s):
    # Regular expression for breaking string into individual characters
    match = re.findall(r'[A-Z0-9]+', s)
    char_list = []
    for i in match:
        if len(char_list) < 82:
            char_list.append(i)
    char_list.sort()
    return char_list
