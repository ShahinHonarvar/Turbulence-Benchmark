
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        sub = s[i:i+30]
        if len(sub) == 30 and len(set(sub)) == 30:
            if sub not in substrings:
                substrings.append(sub)
    return substrings
