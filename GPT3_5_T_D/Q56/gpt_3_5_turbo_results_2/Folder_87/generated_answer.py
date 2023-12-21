
def all_substring_of_size_n(string):
    substrings = []
    for i in range(0, len(string) - 58 + 1):
        substring = string[i:i+58]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings
