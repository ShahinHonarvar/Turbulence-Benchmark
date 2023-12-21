
def all_substring_of_size_124(s):
    substrings = []
    for i in range(len(s) - 123):
        substring = s[i:i+124]
        if len(set(substring)) == 124 and all(ord(c) > 96 and ord(c) < 123 for c in substring):
            substrings.append(substring)
    return substrings
