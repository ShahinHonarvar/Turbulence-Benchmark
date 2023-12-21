
def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 31:
        for i in range(len(string)-30):
            substring = string[i:i+31]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return substrings
