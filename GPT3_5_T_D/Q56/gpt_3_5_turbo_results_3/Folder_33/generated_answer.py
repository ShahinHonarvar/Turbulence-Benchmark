
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 105:
        return substrings
    for i in range(length - 104):
        substring = string[i:i+105]
        if len(set(substring)) == 105:
            substrings.append(substring)
    return substrings
