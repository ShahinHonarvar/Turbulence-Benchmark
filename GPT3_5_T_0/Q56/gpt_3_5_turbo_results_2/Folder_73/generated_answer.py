
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 19):
        substring = string[i:i+20]
        if len(set(substring)) == 20:
            substrings.append(substring)
    return substrings
