
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s)-52):
            substring = s[j:j+53]
            if not any(substring == other for other in substrings):
                substrings.append(substring)
    return substrings
