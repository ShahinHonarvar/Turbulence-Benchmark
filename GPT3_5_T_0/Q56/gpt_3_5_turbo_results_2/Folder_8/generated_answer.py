
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 29):
        substring = string[i:i+30]
        if len(set(substring)) == 30:
            substrings.append(substring)
    return substrings
