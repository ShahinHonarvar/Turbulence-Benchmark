import re
def palindromes_between_indices(s):
    # remove non-alpha characters
    s = re.sub(r'[^A-Za-z]+', '', s)
    # if empty, return empty
    if not s:
        return set()
    # find all possible letter combinations, filter to palindromes
    return set(re.findall(r'((?=([a-z]))[a-z]{1})((?=([a-z]))[a-z]{5})', s))
