
def all_substring_of_size_n(string):
    substrings = []
    size = 106
    for i in range(len(string) - size + 1):
        substring = string[i:i+size]
        if len(set(substring)) == size:
            substrings.append(substring)
    return substrings
