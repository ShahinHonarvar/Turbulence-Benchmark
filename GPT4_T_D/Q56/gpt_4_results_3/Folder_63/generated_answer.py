
def all_substring_of_size_n(s):
    n = 19
    substrings = []
    if n > len(s):
        return []
    for i in range(len(s) - n + 1):
        substring = s[i: i + n]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
