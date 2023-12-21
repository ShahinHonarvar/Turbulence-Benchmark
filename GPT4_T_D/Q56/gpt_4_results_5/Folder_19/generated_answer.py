
def all_substring_of_size_n(s):
    substrings = set()
    n = 18
    for i in range(len(s)):
        if i + n <= len(s):
            substring = s[i:i+n]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
