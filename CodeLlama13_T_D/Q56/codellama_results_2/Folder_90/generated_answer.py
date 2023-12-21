
def all_substring_of_size_130(string):
    substrings = []
    for i in range(len(string) - 129):
        substring = string[i:i+130]
        if len(set(substring)) == 130 and all(c not in substrings for c in substring):
            substrings.append(substring)
    return substrings
