
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 129):
        substring = s[i:i+130]
        if len(set(substring)) == 130 and not any(substring in ss for ss in substrings):
            substrings.append(substring)
    return substrings
