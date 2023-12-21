
def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 41):
        substring = text[i:i+42]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
