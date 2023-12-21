
def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 48:
        for i in range(len(string) - 47):
            substring = string[i:i+48]
            if len(set(substring)) == 48:
                substrings.append(substring)
    return substrings
