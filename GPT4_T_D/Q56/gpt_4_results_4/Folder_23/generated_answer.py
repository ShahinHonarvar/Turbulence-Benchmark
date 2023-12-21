
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 42 > len(s):
            break
        sub = s[i:i+42]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)
