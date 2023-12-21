
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i+50]
        if len(substring) == 50 and len(set(substring)) == 50:
            substrings.add(substring)
    return list(substrings)
