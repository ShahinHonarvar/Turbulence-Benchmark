
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-29):
        substring = s[i:i+30]
        if len(set(substring)) == 30:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
