
def all_substring_of_size_n(s):
    substrings = []
    len_str = len(s)
    for i in range(len_str):
        if i + 61 <= len_str:
            substr = s[i:i+61]
            if len(set(substr)) == len(substr):
                if substr not in substrings:
                    substrings.append(substr)
    return substrings
