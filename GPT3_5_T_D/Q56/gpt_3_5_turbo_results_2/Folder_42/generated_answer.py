
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-44):
        substring = string[i:i+45]
        if len(set(substring)) == 45:
            substrings.append(substring)
    return substrings
