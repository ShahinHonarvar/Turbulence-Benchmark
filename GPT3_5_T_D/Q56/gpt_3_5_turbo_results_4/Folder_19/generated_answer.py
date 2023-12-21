
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 18, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 18 and len(set(substring)) == 18:
                substrings.append(substring)
    return substrings
