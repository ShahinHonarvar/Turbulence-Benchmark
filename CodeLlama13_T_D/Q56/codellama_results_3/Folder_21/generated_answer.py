
def all_substring_of_size_106(s):
    substrings = []
    for i in range(len(s) - 105):
        substring = s[i:i+106]
        if not any(substring.count(c) > 1 for c in substring):
            substrings.append(substring)
    return substrings
