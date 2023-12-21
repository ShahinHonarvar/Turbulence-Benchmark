
def all_substring_of_size_n(s):
    substrings = []

    for i in range(len(s)):
        substring = s[i: i + 110]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
                
    return [substring for substring in substrings if len(substring) == 110]
