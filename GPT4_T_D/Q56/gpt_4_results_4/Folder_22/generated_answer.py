
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 21):
        substring = s[i:i+22]
        if len(set(substring)) == len(list(substring)):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
