
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-95):
        substring = string[i:i+96]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings
