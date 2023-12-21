
from itertools import permutations
import re

def palindromes_between_indices(string):
    letters = re.findall("[a-zA-Z]", string[:3])
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes
