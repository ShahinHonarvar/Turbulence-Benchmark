
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 34 + 1):
        substring = string[i:i+34]
        if not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
