
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 78):
        substring = string[i:i+79]
        if len(set(substring)) == 79:
            substrings.add(substring)
    return list(substrings)
