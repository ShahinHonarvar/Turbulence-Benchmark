
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-16):
        substring = string[i:i+17]
        if len(set(substring)) == 17:
            substrings.append(substring)
    return substrings
