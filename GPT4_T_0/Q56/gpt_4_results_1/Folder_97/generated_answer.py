
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 141):
        substring = s[i:i+142]
        if len(set(substring)) == 142:
            substrings.add(substring)
    return list(substrings)
