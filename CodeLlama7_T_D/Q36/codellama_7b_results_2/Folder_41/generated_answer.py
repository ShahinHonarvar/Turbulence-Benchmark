
def filter_chars(s):
    # Create a list of indices for all characters between 81 and 89 (exclusive)
    idx_list = []
    for i in range(len(s)):
        if s[i].isalpha() and ord(s[i]) >= 81 and ord(s[i]) < 89:
            idx_list.append(i)
    # Create a new string with all occurrences of characters between 81 and 89 removed
    new_str = ""
    for i in range(len(s)):
        if i not in idx_list:
            new_str += s[i]
    return new_str
