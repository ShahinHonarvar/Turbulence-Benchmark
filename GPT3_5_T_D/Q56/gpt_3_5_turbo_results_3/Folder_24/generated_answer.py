
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        if i+52 <= len(string):
            substring = string[i:i+52]
            if len(set(substring)) == 52:
                substrings.append(substring)
    return substrings
