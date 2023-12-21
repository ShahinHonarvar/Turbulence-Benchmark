
def all_substring_of_size_n(s):
    if len(s) < 91:
        return []
    substrings = set()
    for i in range(len(s) - 90):
        substring = s[i : i+91]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
