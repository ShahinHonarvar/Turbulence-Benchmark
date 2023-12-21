
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 31 <= len(s):
            substr = s[i : i + 31]
            if len(set(substr)) == len(substr):
                substrings.add(substr)
    return list(substrings)
