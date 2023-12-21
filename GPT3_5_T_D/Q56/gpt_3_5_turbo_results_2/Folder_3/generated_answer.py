
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 92):
        substring = string[i:i+93]
        if len(set(substring)) == 93:
            substrings.add(substring)
    return list(substrings)
