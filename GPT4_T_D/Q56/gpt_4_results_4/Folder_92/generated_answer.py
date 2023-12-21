
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 9 <= len(s):
            substr = s[i:i+9]
            if len(set(substr)) == len(substr):
                substrings.add(substr)
    return list(substrings)
