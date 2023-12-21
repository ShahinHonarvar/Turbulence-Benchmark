
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 73 <= len(s):
            substring = s[i:i+73]
            if len(set(substring)) == len(substring):
                if substring not in substrings:
                    substrings.append(substring)

    return substrings
