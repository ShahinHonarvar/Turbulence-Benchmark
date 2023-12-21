
def all_substring_of_size_n(s):
    n = 120
    substrings = []
    for i in range(0, len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
