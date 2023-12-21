
def all_substring_of_size_n(s):
    list_substrings = []
    for i in range(len(s)-96):
        substr = s[i:i+97]
        if len(substr) == len(set(substr)) and substr not in list_substrings:
            list_substrings.append(substr)
    return list_substrings
