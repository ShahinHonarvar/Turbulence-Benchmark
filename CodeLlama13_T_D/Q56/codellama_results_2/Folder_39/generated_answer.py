
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 94 + 1):
        substring = string[i:i+94]
        if not any(char in substring for char in substrings):
            substrings.append(substring)
    return substrings
