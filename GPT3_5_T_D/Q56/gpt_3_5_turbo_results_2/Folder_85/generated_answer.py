
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 14 + 1):
        substring = string[i:i+14]
        if len(set(substring)) == 14:
            substrings.append(substring)
    return substrings
