
def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 58:
        for i in range(len(string)-57):
            substring = string[i:i+58]
            if len(set(substring)) == 58:
                substrings.append(substring)
    return substrings
