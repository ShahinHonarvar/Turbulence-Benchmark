
def all_substring_of_size_n(s):
    if len(s) < 90:
        return []
    substrings = set()
    for i in range(len(s) - 89):
        substring = s[i:i+90]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
