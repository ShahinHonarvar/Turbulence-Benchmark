
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 143 <= len(s):
            substring = s[i:i+143]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
