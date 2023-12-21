
def all_substring_of_size_n(s):
    if len(s) < 99:
        return []
    substrings = set()
    for i in range(len(s) - 99 + 1):
        substring = s[i:i+99]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
