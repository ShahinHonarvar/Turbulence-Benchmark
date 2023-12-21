
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 56):
        substring = s[i:i+57]
        if not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
