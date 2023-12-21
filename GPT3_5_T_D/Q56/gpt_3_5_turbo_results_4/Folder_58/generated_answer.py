
def all_substring_of_size_n(string):
    substrings = set()
    if len(string) < 127:
        return []
    for i in range(len(string)-126):
        substring = string[i:i+127]
        if len(set(substring)) == 127:
            substrings.add(substring)
    return list(substrings)
