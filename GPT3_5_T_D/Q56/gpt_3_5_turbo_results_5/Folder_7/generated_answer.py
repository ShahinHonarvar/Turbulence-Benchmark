
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 116):
        substring = string[i:i+117]
        if len(set(substring)) == 117:
            substrings.add(substring)
    return list(substrings)
