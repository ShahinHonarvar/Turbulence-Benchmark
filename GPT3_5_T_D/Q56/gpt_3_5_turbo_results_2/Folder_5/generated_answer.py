
def all_substring_of_size_n(string):
    substrings = set()
    if len(string) < 64:
        return []
    for i in range(len(string)-63):
        if len(set(string[i:i+64])) == 64:
            substrings.add(string[i:i+64])
    return list(substrings)
