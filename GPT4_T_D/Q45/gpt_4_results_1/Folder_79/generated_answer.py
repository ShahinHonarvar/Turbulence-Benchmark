
from itertools import permutations

def palindromes_between_indices(s):
    subset_string = s[1:8]
    permuts = set(["".join(chars) for chars in permutations(subset_string, len(subset_string))])
    result = set()

    for word in permuts:
        if word.lower() == word[::-1].lower() and len(word)>=3:
            result.add(word)

    return result
