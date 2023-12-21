
def all_substring_of_size_n(s):
    substrings = set()

    for i in range(len(s)):
        if i + 96 <= len(s) and len(set(s[i:i+96])) == 96:
            substrings.add(s[i:i+96])

    return list(substrings)
