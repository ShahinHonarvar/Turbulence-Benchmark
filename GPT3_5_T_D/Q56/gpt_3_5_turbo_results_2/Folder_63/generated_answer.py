
def all_substring_of_size_n(s):
    substrings = []
    n = 19
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
