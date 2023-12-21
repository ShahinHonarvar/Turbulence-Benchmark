
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 65 <= len(s):
            substring = s[i:i+65]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
