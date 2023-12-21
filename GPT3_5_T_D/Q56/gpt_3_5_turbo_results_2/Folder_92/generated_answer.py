
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-8):
        substring = s[i:i+9]
        if len(set(substring)) == 9:
            substrings.append(substring)
    return substrings
