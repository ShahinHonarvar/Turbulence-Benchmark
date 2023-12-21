
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-52):
        substring = string[i:i+53]
        if len(set(substring)) == 53:
            if substring not in substrings:
                substrings.append(substring)
    return substrings
