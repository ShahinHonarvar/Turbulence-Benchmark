
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 47 <= len(s):
            substr = s[i:i+47]
            if len(set(substr)) == 47:
                substrings.add(substr)
    return list(substrings)
