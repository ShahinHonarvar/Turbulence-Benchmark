
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j]
            if len(substring) == 96 and not any(c in substring for c in substrings):
                substrings.append(substring)
    return substrings
