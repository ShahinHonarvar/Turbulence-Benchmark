
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 97):
        substring = s[i:i+98]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
