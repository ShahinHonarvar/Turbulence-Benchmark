
def all_substring_of_size_n(string):
    if len(string) < 143:
        return []
    substrings = []
    for i in range(len(string)-142):
        substring = string[i:i+143]
        if len(set(substring)) == 143:
            substrings.append(substring)
    return substrings
