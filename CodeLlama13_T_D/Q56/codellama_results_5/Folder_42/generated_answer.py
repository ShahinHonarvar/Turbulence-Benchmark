
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)-44):
            substr = s[i:j]
            if len(substr) == 45 and not any(c in substr for c in substrings):
                substrings.append(substr)
    return substrings
