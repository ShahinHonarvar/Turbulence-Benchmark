
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 57 + 1):
        substring = string[i:i+67]
        if len(substring) == 67 and not any(c in substrings for c in substring)):
            substrings.append(substring)

    return substrings
