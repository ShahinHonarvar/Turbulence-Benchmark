
def all_substring_of_size_n(s):
    if len(s) < 35:
        return []
    substrings = []
    for i in range(len(s) - 34):
        substring = s[i:i+35]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
