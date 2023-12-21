
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-55):
        substring = s[i:i+56]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
