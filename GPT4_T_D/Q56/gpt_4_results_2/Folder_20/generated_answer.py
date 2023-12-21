
def all_substring_of_size_n(s):
    substrings = []
    substrings_set = set()
    for i in range(len(s)-49):
        substring = s[i:i+50]
        if len(set(substring)) == 50:
            if substring not in substrings_set:
                substrings.append(substring)
                substrings_set.add(substring)
    return substrings
