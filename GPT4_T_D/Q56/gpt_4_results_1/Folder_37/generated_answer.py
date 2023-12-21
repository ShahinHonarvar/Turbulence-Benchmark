
def all_substring_of_size_n(text):
    substrings = set()
    for i in range(0, len(text)-64):
        substring = text[i:i+65]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
