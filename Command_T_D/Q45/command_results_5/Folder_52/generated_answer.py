import re
def palindromes_between_indices(text):
    letters = set(re.findall("[a-z]", text[0:8]))
    return {l for l in (a + b for a in letters for b in letters) if len(l) >= 6 and l[::-1] == l}
