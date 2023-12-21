
def all_substring_of_size_n(s):
    substrings = set()

    for i in range(len(s)):
        substr = s[i:i+46]

        if len(substr) < 46:
            break

        if len(set(substr)) == 46:
            substrings.add(substr)

    return list(substrings)
