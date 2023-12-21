
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 63 + 1):
        substring = string[i:i+63]
        if len(set(substring)) == 63 and not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
