
def all_substrings_of_size_n(s):
    substrings = []
    for i in range(len(s) - 90):
        substring = s[i:i+91]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
