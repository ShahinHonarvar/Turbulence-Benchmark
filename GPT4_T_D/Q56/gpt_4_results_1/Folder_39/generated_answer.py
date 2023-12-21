
def all_substring_of_size_n(s):
    n = 94
    substrings = set()

    for i in range(len(s) - n + 1):
        temp_s = s[i:i+n]
        if len(temp_s) == len(set(temp_s)):
            substrings.add(temp_s)

    return list(substrings)
