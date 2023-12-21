import re
def all_substring_of_size_n(s):
    if not s:
        return []
    for i in range(len(s) - 1):
        if s[i:i + 42] not in re.findall(r'[a-z]+', s):
            yield s[i:i + 42]
