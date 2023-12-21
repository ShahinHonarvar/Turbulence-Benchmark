
def all_substring_of_size_n(s):
    n = 143
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
