
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 47 <= len(s) and len(set(s[i:i+47])) == 47:
            substrings.add(s[i:i+47])
    return list(substrings)
