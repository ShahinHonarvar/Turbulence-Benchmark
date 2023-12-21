
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 27 <= len(s) and len(set(s[i:i+27])) == 27:
            substrings.add(s[i:i+27])
    return list(substrings)
