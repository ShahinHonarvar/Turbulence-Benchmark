import re
def palindromes_between_indices(s):
    letters = re.findall("[a-z]", s)
    return set("".join(sorted(set(letters)) + "".join(sorted(set(letters)))))
