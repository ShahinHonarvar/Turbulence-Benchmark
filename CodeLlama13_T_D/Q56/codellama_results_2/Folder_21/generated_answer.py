
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if not (substring in substrings) and not any(char in substring for char in substrings):
            substrings.append(substring)
    return substrings
