
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, min(len(s), i+100)):
            substring = s[i:j]
            if len(substring) == 100 and all_distinct_chars(substring):
                substrings.append(substring)
    return substrings
