
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 31):
        substring = string[i:i+32]
        if len(set(substring)) == 32:
            substrings.append(substring)
    return substrings
