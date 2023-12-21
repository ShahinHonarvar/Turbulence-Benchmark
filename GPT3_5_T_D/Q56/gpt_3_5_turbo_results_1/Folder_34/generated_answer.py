
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 83):
        substring = string[i:i+84]
        if len(set(substring)) == 84:
            substrings.append(substring)
    return substrings
