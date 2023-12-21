
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 52):
        substring = s[i:i+53]
        if len(set(substring)) == 53:
            substrings.append(substring)
    return list(set(substrings))
