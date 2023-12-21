
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 14:
        return []

    for i in range(len(string)-13):
        substring = string[i:i+14]
        if len(set(substring)) == 14:
            substrings.append(substring)

    return substrings
