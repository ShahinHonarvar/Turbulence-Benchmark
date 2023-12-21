
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 96):
        substring = string[i:i+97]
        if len(set(substring)) == 97 and not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
