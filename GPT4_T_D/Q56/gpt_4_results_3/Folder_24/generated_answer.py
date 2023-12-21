
def all_substring_of_size_n(s):
    substrings = []

    for i in range(len(s)):
        substring = s[i:i+52]
        if len(substring) == 52 and len(set(substring)) == 52:
            if substring not in substrings:
                substrings.append(substring)

    return substrings
