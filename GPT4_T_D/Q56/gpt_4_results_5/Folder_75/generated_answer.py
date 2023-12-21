
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 16 <= len(s):
            substring = s[i:i+16]
            if len(set(substring)) == len(substring):
                if substring not in substrings:
                    substrings.append(substring)
    return substrings
