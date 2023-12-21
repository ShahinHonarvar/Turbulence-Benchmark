
def all_substring_of_size_n(s):
    n = 52
    substrings = []
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if len(set(substr)) == n and not any(substr[j] == substr[j-1] for j in range(1, n)):
            substrings.append(substr)
    return substrings
