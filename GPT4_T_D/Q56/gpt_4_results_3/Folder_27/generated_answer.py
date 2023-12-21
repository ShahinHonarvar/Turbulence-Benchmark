
def all_substring_of_size_n(s):
    if len(s) < 57:
        return []
    substrings = []
    for i in range(len(s) - 56):
        substring = s[i:i+57]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
