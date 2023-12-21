
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 105):
        substring = string[i:i+106]
        if len(set(substring)) == 106:
            substrings.add(substring)
    return list(substrings)
