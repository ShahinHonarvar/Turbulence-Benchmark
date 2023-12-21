
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 42):
        substring = s[i:i+43]
        if len(set(substring)) == 43:
            substrings.append(substring)
    return list(set(substrings))
