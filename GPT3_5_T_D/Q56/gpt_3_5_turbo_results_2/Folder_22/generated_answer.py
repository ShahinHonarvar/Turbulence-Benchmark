
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 21):
        substring = string[i:i+22]
        if len(set(substring)) == 22:
            substrings.add(substring)
    return list(substrings)
