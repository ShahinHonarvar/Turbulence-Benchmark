
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-40):
        substring = string[i:i+41]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings
