
def all_substring_of_size_n(s):
    if len(s) < 21:
        return []
    substrings = []
    for i in range(len(s) - 20):
        substring = s[i:i+21]
        if len(set(substring)) == 21:
            substrings.append(substring)
    return list(set(substrings))
