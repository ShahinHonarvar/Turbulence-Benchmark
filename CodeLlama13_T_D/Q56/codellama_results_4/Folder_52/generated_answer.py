
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 14):
        substring = string[i:i+15]
        if len(set(substring)) == 15 and not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
