
def all_substring_of_size_n(string):
    if len(string) < 61:
        return []
    substrings = []
    for i in range(len(string) - 60):
        substring = string[i:i+61]
        if len(set(substring)) == 61:
            substrings.append(substring)
    return substrings
