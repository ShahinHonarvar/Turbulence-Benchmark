
def all_substring_of_size_n(string):
    substrings = set()
    if len(string) >= 52:
        for i in range(len(string)-51):
            substring = string[i:i+52]
            if len(set(substring)) == 52:
                substrings.add(substring)
    return list(substrings)
