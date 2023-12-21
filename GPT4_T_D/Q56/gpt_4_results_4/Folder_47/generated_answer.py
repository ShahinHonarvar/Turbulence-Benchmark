
def all_substring_of_size_n(s):
    substring_set = set()
    for i in range(len(s)):
        if i + 91 <= len(s) and len(set(s[i:i+91])) == 91:
            substring_set.add(s[i:i+91])
    return list(substring_set)
