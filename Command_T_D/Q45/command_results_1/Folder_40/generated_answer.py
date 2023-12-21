import re
def palindromes_between_indices(s):
    idx = 4
    end = 9
    while idx < end:
        match = re.fullmatch(r'[a-z]+', s[idx:end])
        if match:
            idx += match.end()
            end = idx
            break
    return set(re.findall(r'([a-z]+)[a-z]+', s[idx:end]))
