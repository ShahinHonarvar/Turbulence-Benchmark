
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(set(s[i:i+90])) == 90:
            substrings.add(s[i:i+90])
    return list(substrings)
