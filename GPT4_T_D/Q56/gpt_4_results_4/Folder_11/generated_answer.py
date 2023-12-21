
def all_substring_of_size_n(text):
    if len(text) < 78:
        return []
    substrings = set()
    for i in range(len(text) - 77):
        substring = text[i:i+78]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
