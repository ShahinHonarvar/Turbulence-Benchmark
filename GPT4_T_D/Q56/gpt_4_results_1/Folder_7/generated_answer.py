
def all_substring_of_size_n(s):
    substrings = []
    seen = set()
    for i in range(len(s) - 116):
        substr = s[i:i+117]
        if len(substr) == len(set(substr)):
            if substr not in seen:
                substrings.append(substr)
                seen.add(substr)
    return substrings
