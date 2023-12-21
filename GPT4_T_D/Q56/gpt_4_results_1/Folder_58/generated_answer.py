
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)-126):
        substring = s[i:i+127]
        if len(set(substring)) == 127:
            substrings.add(substring)
    return list(substrings)
