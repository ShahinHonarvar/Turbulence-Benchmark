
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-98):
        substring = string[i:i+99]
        if len(set(substring)) == 99:
            substrings.append(substring)
    return substrings
