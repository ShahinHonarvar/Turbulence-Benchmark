
def all_substring_of_size_n(string):
    unique_substrings = []
    for i in range(len(string)-30):
        substring = string[i:i+31]
        if len(set(substring)) == len(substring):
            unique_substrings.append(substring)
    return unique_substrings
