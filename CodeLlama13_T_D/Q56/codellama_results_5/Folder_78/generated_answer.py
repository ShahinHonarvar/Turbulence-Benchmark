
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-49+1):
        substr = s[i:i+49]
        if len(set(substr)) == 49 and not any(substr[j] in substr[:j] for j in range(len(substr))):
            substrings.append(substr)
    return substrings
