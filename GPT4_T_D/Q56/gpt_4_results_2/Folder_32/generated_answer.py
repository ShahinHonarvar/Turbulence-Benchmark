
def all_substring_of_size_n(s):
    if len(s)<71:
        return []
    substrings = []
    for i in range(len(s)-70):
        substring = s[i:i+71]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))
