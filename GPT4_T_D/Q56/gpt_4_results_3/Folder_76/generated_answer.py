
def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s)):
        if i + 149 <= len(s):
            substr = s[i: i + 149]
            if len(substr) == len(set(substr)):
                if substr not in subs:
                    subs.append(substr)
    return subs
