
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 10):
        substring = string[i:i+11]
        if len(set(substring)) == 11:
            substrings.add(substring)
    return list(substrings)
