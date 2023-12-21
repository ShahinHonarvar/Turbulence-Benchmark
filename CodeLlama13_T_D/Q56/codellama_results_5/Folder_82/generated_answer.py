
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string), 100):
            substring = string[i:j]
            if not any(substring == s for s in substrings) and all(substring != s for s in substrings):
                substrings.append(substring)
    return substrings
