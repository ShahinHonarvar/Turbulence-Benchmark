
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 34 <= len(s):
            substring = s[i:i + 34]
            if len(set(substring)) == len(substring):
                if substring not in substrings:
                    substrings.append(substring)
    return substrings
