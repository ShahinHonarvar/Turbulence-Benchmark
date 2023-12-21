
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)-18):
        substring = string[i:i+19]
        if len(set(substring)) == 19:
            substrings.add(substring)
    return list(substrings)
