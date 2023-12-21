
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)-78):
        substring = s[i:i+79]
        if len(set(substring)) == 79:
            substrings.add(substring)
    return list(substrings)
