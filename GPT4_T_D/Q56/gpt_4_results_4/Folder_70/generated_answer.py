
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i+12]
        if len(substring) == 12 and len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
