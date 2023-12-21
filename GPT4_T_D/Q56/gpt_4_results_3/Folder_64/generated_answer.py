
def all_substring_of_size_n(str):
    substrings = []
    for i in range(len(str) - 7):
        substr = str[i:i+8]
        if len(substr) == len(set(substr)):
            if substr not in substrings:
                substrings.append(substr)
    return substrings
