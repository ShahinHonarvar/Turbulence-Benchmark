
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        substring = string[i:i+79]
        if len(substring) == 79 and len(set(substring)) == 79:
            substrings.append(substring)
    return substrings
