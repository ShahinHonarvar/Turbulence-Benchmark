
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 63 <= len(s):
            substring = s[i:i+63]
            if len(substring) == len(set(substring)):
                substrings.add(substring)
    return list(substrings)
