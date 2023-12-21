
def all_substring_of_size_n(s):
    n = 37
    substrings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == n]
    distinct_substrings = []
    for substring in substrings:
        if len(set(substring)) == n:
            if substring not in distinct_substrings:
                distinct_substrings.append(substring)
    return distinct_substrings
