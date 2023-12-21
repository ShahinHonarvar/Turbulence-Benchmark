
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 15):
        substring = string[i:i+16]
        if len(set(substring)) == 16:
            substrings.append(substring)
    return substrings
